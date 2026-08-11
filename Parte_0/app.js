const $=(selector)=>document.querySelector(selector);
const $$=(selector)=>[...document.querySelectorAll(selector)];
const blank={tech:{},diagnostic:null,seed:{},agreement:{}};
let state={...blank,...JSON.parse(localStorage.getItem('si_parte0')||'{}')};

function save(){localStorage.setItem('si_parte0',JSON.stringify(state));updateProgress()}
function completion(){
  const tech=Object.values(state.tech||{}).filter(Boolean).length/8;
  const diagnostic=state.diagnostic?1:0;
  const seedFields=['user','problem','decision','evidence','limits','simple'];
  const seed=((state.seed?.domain||'').trim()?1:0)+seedFields.filter(k=>(state.seed?.[k]||'').trim().length>12).length;
  const agreement=Object.values(state.agreement||{}).filter(Boolean).length/6;
  return Math.round((tech+diagnostic+seed/7+agreement)/4*100);
}
function updateProgress(){const value=completion();$('#progressBar').style.width=value+'%';$('#progressText').textContent=value+' %'}
function show(id){
  $$('.panel').forEach(panel=>panel.classList.toggle('active',panel.id===id));
  $$('.nav button').forEach(button=>button.classList.toggle('active',button.dataset.target===id));
  const panel=$('#'+id); if(panel){panel.focus();history.replaceState(null,'','#'+id)}
}
$$('.nav button').forEach(button=>button.addEventListener('click',()=>show(button.dataset.target)));
$$('.next').forEach(button=>button.addEventListener('click',()=>show(button.dataset.next)));

$$('[data-tech]').forEach(box=>{
  box.checked=Boolean(state.tech?.[box.dataset.tech]);
  box.addEventListener('change',()=>{state.tech[box.dataset.tech]=box.checked;save();renderTech()});
});
function renderTech(){
  const count=Object.values(state.tech||{}).filter(Boolean).length;
  const missing=$$('[data-tech]').filter(box=>!box.checked).map(box=>box.parentElement.textContent.trim());
  const result=$('#techResult');result.className='result show '+(count===8?'good':count>=5?'warn':'bad');
  result.innerHTML=`<h3>${count}/8 comprobaciones listas</h3><p>${count===8?'Tu entorno básico está preparado. Conserva una copia local de los materiales importantes.':count>=5?'Tienes una base suficiente, pero conviene resolver los accesos pendientes antes del laboratorio.':'Necesitas apoyo inicial. Lleva esta lista al encuadre para definir una alternativa.'}</p>${missing.length?`<details><summary>Aspectos pendientes (${missing.length})</summary><ul>${missing.map(item=>`<li>${item}</li>`).join('')}</ul></details>`:''}`;
}

const diagnostic=[
  {area:'Conceptual',q:'Una lámpara se enciende todos los días a las 19:00. ¿Qué describe mejor el caso?',a:['Agente que aprende','Automatización por regla temporal','Modelo predictivo'],ok:1,why:'Ejecuta una condición predefinida; no necesita inferir ni aprender.'},
  {area:'Conceptual',q:'¿Qué hace principalmente un modelo dentro de un sistema?',a:['Transforma entradas en estimaciones o salidas','Define por sí solo todas las responsabilidades','Sustituye siempre a una persona'],ok:0,why:'Un modelo es un componente; el sistema incluye además datos, interfaz, reglas y operación.'},
  {area:'Conceptual',q:'¿Cuál describe mejor a un agente?',a:['Almacena archivos','Percibe y selecciona acciones orientadas a un objetivo','Solo produce texto'],ok:1,why:'La agencia conecta percepción, decisión y acción.'},
  {area:'Conceptual',q:'Si falta información indispensable, una conducta responsable puede ser...',a:['Inventar el dato más probable','Abstenerse y solicitar revisión','Ocultar la incertidumbre'],ok:1,why:'La abstención evita actuar con evidencia insuficiente.'},
  {area:'Conceptual',q:'¿Qué criterio es más útil para evaluar un sistema?',a:['Que se vea moderno','Que cumpla el objetivo y controle daños','Que use la herramienta más nueva'],ok:1,why:'El desempeño debe vincular utilidad, error y posibles consecuencias.'},
  {area:'Conceptual',q:'¿Cuándo puede ser correcto no usar IA?',a:['Cuando una regla simple resuelve el problema con menor riesgo','Nunca','Solo cuando no hay internet'],ok:0,why:'La proporcionalidad exige justificar por qué la IA aporta valor frente a una solución más simple.'},
  {area:'Digital',q:'Antes de modificar una plantilla, lo más seguro es...',a:['Conservar una copia original','Borrar las instrucciones','Cambiar varias cosas al mismo tiempo'],ok:0,why:'Una copia permite comparar, recuperar y documentar cambios.'},
  {area:'Digital',q:'En un notebook, una celda de código...',a:['Puede ejecutarse y producir una salida','Es únicamente una imagen','Siempre modifica tu computadora'],ok:0,why:'Las celdas ejecutan instrucciones en el entorno del notebook.'},
  {area:'Digital',q:'Si aparece un error después de cambiar un parámetro, conviene primero...',a:['Ocultarlo','Leer el mensaje y comparar el cambio con la versión funcional','Reinstalar todo'],ok:1,why:'Aislar el cambio y leer la traza facilita localizar la causa.'},
  {area:'Digital',q:'¿Qué nombre conserva mejor la trazabilidad?',a:['final_final2.ipynb','AgenteConfort_U1_v02_2026-08-24.ipynb','archivo.ipynb'],ok:1,why:'Un nombre con artefacto, versión y fecha permite ordenar el proceso.'},
  {area:'Digital',q:'Para entregar un ZIP correctamente debes...',a:['Comprobar que abre y contiene los archivos solicitados','Cambiarle la extensión a PDF','Enviar solo una captura'],ok:0,why:'La verificación evita carpetas vacías o rutas incorrectas.'},
  {area:'Digital',q:'Si una plataforma no está disponible, la acción más adecuada es...',a:['Esperar hasta después del cierre','Documentar el problema y usar la alternativa indicada','Copiar la evidencia de otra persona'],ok:1,why:'La comunicación oportuna y la alternativa mantienen la trazabilidad.'}
];
$('#diagnosticQuestions').innerHTML=diagnostic.map((item,index)=>`<fieldset class="question"><legend>${index+1}. <small>${item.area}</small> · ${item.q}</legend>${item.a.map((answer,j)=>`<label><input type="radio" name="d${index}" value="${j}" required> ${answer}</label>`).join('')}<div class="feedback" id="df${index}"></div></fieldset>`).join('');
$('#diagnosticForm').addEventListener('submit',event=>{
  event.preventDefault();const data=new FormData(event.target);let conceptual=0,digital=0;
  diagnostic.forEach((item,index)=>{const answer=Number(data.get('d'+index));const ok=answer===item.ok;if(ok){if(index<6)conceptual++;else digital++}$('#df'+index).innerHTML=`<span class="${ok?'correct':'incorrect'}">${ok?'Correcto.':'Revisa.'}</span> ${item.why}`});
  state.diagnostic={conceptual,digital,date:new Date().toISOString()};save();renderDiagnostic();
});
function level(score){return score>=5?'base sólida':score>=3?'base en desarrollo':'apoyo inicial recomendado'}
function renderDiagnostic(){if(!state.diagnostic)return;const {conceptual,digital}=state.diagnostic;const result=$('#diagnosticResult');result.className='result show '+(conceptual>=5&&digital>=5?'good':'warn');result.innerHTML=`<h3>Tu perfil inicial</h3><div class="profile"><p><strong>Comprensión conceptual:</strong> ${conceptual}/6 · ${level(conceptual)}</p><p><strong>Autonomía digital:</strong> ${digital}/6 · ${level(digital)}</p></div><p>Este perfil no es una etiqueta. Se comparará con tus evidencias posteriores para observar progreso.</p>`}

const seedForm=$('#seedForm');
Object.entries(state.seed||{}).forEach(([key,value])=>{if(seedForm.elements[key])seedForm.elements[key].value=value});
seedForm.addEventListener('input',()=>{state.seed=Object.fromEntries(new FormData(seedForm));save()});
seedForm.addEventListener('reset',()=>{setTimeout(()=>{state.seed={};save();$('#seedResult').className='result'},0)});
function reviewSeed(){
  state.seed=Object.fromEntries(new FormData(seedForm));const checks=[['Ámbito definido',state.seed.domain],['Usuario descrito sin datos personales',(state.seed.user||'').length>25],['Problema observable y contextualizado',(state.seed.problem||'').length>40],['Decisión o tarea delimitada',(state.seed.decision||'').length>25],['Evidencia posible identificada',(state.seed.evidence||'').length>25],['Límites iniciales explícitos',(state.seed.limits||'').length>25],['Alternativa simple considerada',(state.seed.simple||'').length>25]];const count=checks.filter(([,ok])=>Boolean(ok)).length;const result=$('#seedResult');result.className='result show '+(count===7?'good':'warn');result.innerHTML=`<h3>${count}/7 elementos listos</h3><ul>${checks.map(([label,ok])=>`<li>${ok?'✓':'△'} ${label}</li>`).join('')}</ul><p>${count===7?'La semilla está lista para descargarse y revisarse en la Unidad I.':'Completa los elementos marcados con △ antes de descargar.'}</p>`;save();return count;
}
$('#reviewSeed').addEventListener('click',reviewSeed);
$('#downloadSeed').addEventListener('click',()=>{const count=reviewSeed();if(count<7)return;const s=state.seed;download('Semilla_Proyecto_Sistemas_Inteligentes.txt',`SEMILLA DEL PROYECTO INTEGRADOR\n\nÁmbito: ${s.domain}\nUsuario o grupo: ${s.user}\n\nSituación problemática:\n${s.problem}\n\nDecisión o tarea que podría apoyarse:\n${s.decision}\n\nEvidencia necesaria:\n${s.evidence}\n\nQué no debe automatizarse:\n${s.limits}\n\nPor qué una solución simple quizá bastaría:\n${s.simple}\n\nNota: propuesta preliminar para someter a análisis de pertinencia y PEAS en la Unidad I.\n`)});

$$('[data-agree]').forEach(box=>{box.checked=Boolean(state.agreement?.[box.dataset.agree]);box.addEventListener('change',()=>{state.agreement[box.dataset.agree]=box.checked;save();renderAgreement()})});
function renderAgreement(){const count=Object.values(state.agreement||{}).filter(Boolean).length;const result=$('#agreementResult');result.className='result show '+(count===6?'good':'warn');result.innerHTML=`<h3>${count}/6 compromisos confirmados</h3><p>${count===6?'Has completado el acuerdo de trabajo. Descarga el resumen de inducción.':'Lee y confirma los compromisos restantes; anota cualquier duda para el encuadre.'}</p>`}

function download(filename,text){const link=document.createElement('a');link.href=URL.createObjectURL(new Blob([text],{type:'text/plain;charset=utf-8'}));link.download=filename;link.click();URL.revokeObjectURL(link.href)}
$('#downloadSummary').addEventListener('click',()=>{const d=state.diagnostic||{conceptual:'pendiente',digital:'pendiente'};download('Resumen_Induccion_Sistemas_Inteligentes.txt',`RESUMEN DE INDUCCIÓN · SISTEMAS INTELIGENTES\n\nProgreso: ${completion()} %\nPreparación tecnológica: ${Object.values(state.tech||{}).filter(Boolean).length}/8\nDiagnóstico conceptual: ${d.conceptual}/6\nDiagnóstico digital: ${d.digital}/6\nSemilla de proyecto: ${state.seed?.problem?'iniciada':'pendiente'}\nAcuerdo de trabajo: ${Object.values(state.agreement||{}).filter(Boolean).length}/6\n\nEste resumen es para autoseguimiento; no contiene una calificación.\n`)});
$('#printSummary').addEventListener('click',()=>print());
$('#resetAll').addEventListener('click',()=>{if(confirm('¿Deseas borrar la preparación, el diagnóstico y la semilla guardados en este dispositivo?')){localStorage.removeItem('si_parte0');location.reload()}});

renderTech();renderDiagnostic();renderAgreement();updateProgress();const initial=location.hash.slice(1);if($(`#${initial}.panel`))show(initial);
