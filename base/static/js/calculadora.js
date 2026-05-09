function atualizarCampos() {
    const tipo = document.getElementById("tipoMedia").value;
    const camposBimestral = document.getElementById("camposBimestral");
    const camposExame = document.getElementById("camposExame");

    if (tipo === "bimestral") {
        camposBimestral.style.display = "block";
        camposExame.style.display = "none";
    } else {
        camposBimestral.style.display = "none";
        camposExame.style.display = "block";
    }
}

window.onload = atualizarCampos;

function calcularMedia(event) {
    event.preventDefault();

    const tipo = document.getElementById("tipoMedia").value;
    const resultado = document.getElementById("resultado");

    if (tipo === "bimestral") {
        const notaAtividades = parseFloat(document.getElementById("notaAtividades").value) || 0;
        const notaProva = parseFloat(document.getElementById("notaProvaBimestral").value) || 0;

        const media = (notaAtividades * 0.4 + notaProva * 0.6);
        resultado.innerHTML = `Média Bimestral: ${media.toFixed(2)}`;
    } else {
        const mediaAva = parseFloat(document.getElementById("mediaBimestral").value) || 0;
        const notaExame = parseFloat(document.getElementById("notaExame").value) || 0;
        if (mediaAva >= 5) {
            resultado.innerHTML = `Você já está APROVADO`; 
        } else {
            const media = (mediaAva * 0.5 + notaExame * 0.5);
            resultado.innerHTML = `Média Final: ${media.toFixed(2)}`;
        }

        
    }
}