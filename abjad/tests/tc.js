(function(){
  var KP='abjad-tc:';
  function sel(){var s=document.createElement('select');s.className='st';
    ['Not Run','Pass','Fail','Blocked'].forEach(function(o){var op=document.createElement('option');op.textContent=o;s.appendChild(op);});return s;}
  // free-text meta fields (tester name/date/build) persisted by data-id
  document.querySelectorAll('[data-id]').forEach(function(el){
    var k=KP+el.getAttribute('data-id');var v=localStorage.getItem(k);
    if(v!==null)el.textContent=v;
    el.addEventListener('input',function(){localStorage.setItem(k,el.textContent);});
  });
  // build status + notes cells for every test row, wire persistence keyed by case ID
  document.querySelectorAll('table.tc tbody tr').forEach(function(tr){
    var idCell=tr.querySelector('td.id');if(!idCell)return;var id=idCell.textContent.trim();
    var p=tr.getAttribute('data-p')||'M';
    var pc=document.createElement('td');pc.className='pcell';
    pc.innerHTML='<span class="pri '+p+'" title="'+({C:'Critical',H:'High',M:'Medium',L:'Low'}[p]||'')+'">'+p+'</span>';
    idCell.after(pc);
    var sc=document.createElement('td');sc.className='stcell';var s=sel();
    var sk=KP+id+':st',sv=localStorage.getItem(sk);if(sv)s.value=sv;s.setAttribute('data-v',s.value);
    s.addEventListener('change',function(){localStorage.setItem(sk,s.value);s.setAttribute('data-v',s.value);prog();});
    sc.appendChild(s);tr.appendChild(sc);
    var nc=document.createElement('td');nc.className='ncell';var n=document.createElement('div');
    n.className='note-cell';n.contentEditable=true;
    var nk=KP+id+':note',nv=localStorage.getItem(nk);if(nv!==null)n.textContent=nv;
    n.addEventListener('input',function(){localStorage.setItem(nk,n.textContent);});
    nc.appendChild(n);tr.appendChild(nc);
  });
  window.prog=function(){
    var s=document.querySelectorAll('table.tc select.st'),t=s.length,p=0,f=0,b=0,r=0;
    s.forEach(function(x){if(x.value!=='Not Run')r++;if(x.value==='Pass')p++;if(x.value==='Fail')f++;if(x.value==='Blocked')b++;});
    var e=document.getElementById('prog');if(e)e.textContent=r+'/'+t+' run · '+p+' pass · '+f+' fail · '+b+' blocked';
  };
  window.exportResults=function(){
    var o={cases:[]};
    document.querySelectorAll('[data-id]').forEach(function(el){o[el.getAttribute('data-id')]=el.textContent;});
    document.querySelectorAll('table.tc tbody tr').forEach(function(tr){
      var i=tr.querySelector('td.id');if(!i)return;var s=tr.querySelector('select.st'),n=tr.querySelector('.note-cell');
      o.cases.push({id:i.textContent.trim(),status:s?s.value:'',notes:n?n.textContent:''});
    });
    var b=new Blob([JSON.stringify(o,null,2)],{type:'application/json'});
    var a=document.createElement('a');a.href=URL.createObjectURL(b);
    a.download='abjad-test-results-'+new Date().toISOString().slice(0,10)+'.json';a.click();
  };
  // whole-book export scans localStorage for every saved case (used on index page)
  window.exportAll=function(){
    var o={};for(var i=0;i<localStorage.length;i++){var k=localStorage.key(i);if(k.indexOf(KP)===0)o[k.slice(KP.length)]=localStorage.getItem(k);}
    var b=new Blob([JSON.stringify(o,null,2)],{type:'application/json'});
    var a=document.createElement('a');a.href=URL.createObjectURL(b);
    a.download='abjad-test-results-all-'+new Date().toISOString().slice(0,10)+'.json';a.click();
  };
  // --- repository persistence: tests/results.json ---
  // ponytail: auto-save via File System Access API — one-time file pick, then every edit writes to tests/results.json
  var fileHandle=null,connected=false,saveTimer=null;
  function dump(){var o={};for(var i=0;i<localStorage.length;i++){var k=localStorage.key(i);if(k.indexOf(KP)===0)o[k.slice(KP.length)]=localStorage.getItem(k);}return o;}
  function flash(msg){var d=document.createElement('div');d.className='tc-toast';d.textContent=msg;document.body.appendChild(d);setTimeout(function(){d.remove();},4000);}

  // tiny IndexedDB kv — localStorage can't hold a file handle
  function idb(){return new Promise(function(res,rej){var q=indexedDB.open('abjad-tc',1);
    q.onupgradeneeded=function(){q.result.createObjectStore('kv');};
    q.onsuccess=function(){res(q.result);};q.onerror=function(){rej(q.error);};});}
  function idbSet(k,v){return idb().then(function(db){return new Promise(function(res){var t=db.transaction('kv','readwrite');t.objectStore('kv').put(v,k);t.oncomplete=res;});});}
  function idbGet(k){return idb().then(function(db){return new Promise(function(res){var r=db.transaction('kv').objectStore('kv').get(k);r.onsuccess=function(){res(r.result);};r.onerror=function(){res(null);};});});}

  var bar=document.createElement('div');bar.id='repo-bar';document.body.appendChild(bar);
  function setBar(html,cls){bar.innerHTML=html;bar.className=cls||'';}

  async function writeFile(){
    try{var w=await fileHandle.createWritable();await w.write(JSON.stringify(dump(),null,2));await w.close();
      setBar('<span class="pill ok">✓ Auto-saving to results.json</span>');}
    catch(e){connected=false;setBar('<button onclick="tcResume()">⚠ Auto-save lost — click to reconnect</button>','warn');}
  }
  function scheduleSave(){if(!connected)return;clearTimeout(saveTimer);saveTimer=setTimeout(writeFile,800);}
  // pull results already in the file (from another tester/machine); browser's own edits win
  async function mergeFromFile(){
    try{var o=JSON.parse(await (await fileHandle.getFile()).text());var added=0;
      Object.keys(o).forEach(function(k){if(localStorage.getItem(KP+k)===null){localStorage.setItem(KP+k,o[k]);added++;}});
      if(added){flash('Loaded '+added+' saved result(s) from results.json');setTimeout(function(){location.reload();},700);}}
    catch(e){}
  }
  window.tcConnect=async function(){
    try{
      var h=(await showOpenFilePicker({types:[{description:'JSON results',accept:{'application/json':['.json']}}]}))[0];
      if((await h.requestPermission({mode:'readwrite'}))!=='granted')return;
      fileHandle=h;await idbSet('handle',h);connected=true;
      await mergeFromFile();await writeFile();
      flash('Connected — every change now saves to results.json automatically');
    }catch(e){if(e.name!=='AbortError')flash('Could not connect: '+e.message);}
  };
  window.tcResume=async function(){
    if((await fileHandle.requestPermission({mode:'readwrite'}))==='granted'){connected=true;await mergeFromFile();await writeFile();}
  };
  window.tcDownload=function(){
    var b=new Blob([JSON.stringify(dump(),null,2)],{type:'application/json'});
    var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='results.json';a.click();
    flash('Downloaded — replace abjad/tests/results.json with it and commit');
  };

  if(window.showOpenFilePicker){
    idbGet('handle').then(async function(h){
      if(h){fileHandle=h;
        var p=await h.queryPermission({mode:'readwrite'});
        if(p==='granted'){connected=true;await mergeFromFile();writeFile();}
        else setBar('<button onclick="tcResume()">▶ Resume auto-save to results.json</button>','warn');
      }else setBar('<button onclick="tcConnect()" title="Pick abjad/tests/results.json once — after that every change saves automatically">⚡ Connect results.json (one-time)</button>');
    });
  }else{
    // Safari/Firefox fallback: no silent file writes possible — manual download
    setBar('<button onclick="tcDownload()">💾 Download results.json</button>');
  }

  // any edit anywhere → debounced auto-save (status selects, notes, tester meta)
  document.addEventListener('change',function(e){if(e.target&&e.target.classList&&e.target.classList.contains('st'))scheduleSave();},true);
  document.addEventListener('input',function(e){if(e.target&&e.target.closest&&e.target.closest('[contenteditable],[data-id]'))scheduleSave();},true);

  prog();
})();
