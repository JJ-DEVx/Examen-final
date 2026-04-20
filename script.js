<<<<<<< HEAD
const API = "https://talleres-api-myx2.onrender.com/workshops";

// Cargar talleres
fetch(API)
.then(res => res.json())
.then(data => {
    const div = document.getElementById("workshops");

    div.innerHTML = ""; // limpiar

    data.forEach(w => {
        div.innerHTML += `
        <div class="col-md-4">
            <div class="card mb-4 shadow">
                <div class="card-body">
                    <h5 class="card-title">${w.name}</h5>
                    
                    <p class="card-text">
                        ${w.description || "Sin descripcion"}
                    </p>

                    <p><strong>Fecha:</strong> ${w.date}</p>
                    <p><strong>Hora:</strong> ${w.time}</p>
                    <p><strong>Lugar:</strong> ${w.place}</p>
                    <p><strong>Categoria:</strong> ${w.category}</p>

                    <button class="btn btn-primary w-100"
                        onclick="register(${w.id})">
                        Inscribirse
                    </button>
                </div>
            </div>
        </div>
        `;
    });
});


// Registrar estudiante
function register(id){
    const name = prompt("Ingresa tu nombre:");

    if(!name || name.trim() === ""){
        alert("Debes ingresar un nombre válido");
        return;
    }

    fetch(API + "/" + id + "/register", {
        method: "POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({name:name})
    })
    .then(res => res.json())
    .then(data => {
        alert("Te has registrado correctamente");
    });
=======
const API = "http://127.0.0.1:5000/workshops";

// Cargar talleres
fetch(API)
.then(res => res.json())
.then(data => {
    const div = document.getElementById("workshops");

    div.innerHTML = ""; // limpiar

    data.forEach(w => {
        div.innerHTML += `
        <div class="col-md-4">
            <div class="card mb-4 shadow">
                <div class="card-body">
                    <h5 class="card-title">${w.name}</h5>
                    
                    <p class="card-text">
                        ${w.description || "Sin descripcion"}
                    </p>

                    <p><strong>Fecha:</strong> ${w.date}</p>
                    <p><strong>Hora:</strong> ${w.time}</p>
                    <p><strong>Lugar:</strong> ${w.place}</p>
                    <p><strong>Categoria:</strong> ${w.category}</p>

                    <button class="btn btn-primary w-100"
                        onclick="register(${w.id})">
                        Inscribirse
                    </button>
                </div>
            </div>
        </div>
        `;
    });
});


// Registrar estudiante
function register(id){
    const name = prompt("Ingresa tu nombre:");

    if(!name || name.trim() === ""){
        alert("Debes ingresar un nombre válido");
        return;
    }

    fetch(API + "/" + id + "/register", {
        method: "POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({name:name})
    })
    .then(res => res.json())
    .then(data => {
        alert("Te has registrado correctamente");
    });
>>>>>>> 56e814f15d8c66ed8a42f98983505eb945d62847
}