const API = "https://talleres-api-myx2.onrender.com/workshops";

fetch(API)
    .then(res => res.json())
    .then(data => {
        const container = document.getElementById("workshops");

        data.forEach(w => {
            container.innerHTML += `
                <div class="col-md-4">
                    <div class="card mb-3">
                        <div class="card-body">
                            <h5>${w.name}</h5>
                            <p>${w.description}</p>
                            <p><b>Fecha:</b> ${w.date}</p>
                            <p><b>Lugar:</b> ${w.place}</p>
                            <button class="btn btn-primary" onclick="inscribirse(${w.id})">Inscribirse</button>
                        </div>
                    </div>
                </div>
            `;
        });
    });

function inscribirse(id){
    const nombre = prompt("Tu nombre:");

    fetch(API + "/" + id + "/register", {
        method: "POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({name: nombre})
    })
    .then(() => alert("Registrado"));
}