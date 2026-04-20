const API = "https://talleres-api-myx2.onrender.com/workshops";

async function cargar() {
    const res = await fetch(API);
    const data = await res.json();

    const container = document.getElementById("workshops");
    container.innerHTML = "";

    data.forEach(w => {
        container.innerHTML += `
            <div class="col-md-4">
                <div class="card mb-4 shadow-sm border-0">
                    <div class="card-body">

                        <h5 class="card-title text-primary">${w.name}</h5>

                        <p class="text-muted">${w.description}</p>

                        <p>📅 <b>Fecha:</b> ${formatearFecha(w.date)}</p>
                        <p>🕒 <b>Hora:</b> ${formatearHora(w.time)}</p>
                        <p>📍 <b>Lugar:</b> ${w.place}</p>

                        <button class="btn btn-success w-100" onclick="inscribirse(${w.id})">
                            Inscribirse
                        </button>

                    </div>
                </div>
            </div>
        `;
    });
}

function inscribirse(id){
    const nombre = prompt("Ingrese su nombre:");

    if(!nombre){
        alert("Debe ingresar un nombre");
        return;
    }

    fetch(API + "/" + id + "/register", {
        method: "POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({name: nombre})
    })
    .then(() => alert("Registrado correctamente"));
}

function formatearFecha(fecha){
    const f = new Date(fecha);
    return f.toLocaleDateString("es-ES");
}

function formatearHora(hora){
    if(!hora) return "";
    return hora.slice(0,5);
}

cargar();