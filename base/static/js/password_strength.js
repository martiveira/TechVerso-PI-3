// Função para verificar a força da senha
function checkPasswordStrength(password) {
    let strength = 0;

    // Requisitos da senha
    const lengthRule = /^(?=.{8,})/;  // Pelo menos 8 caracteres
    const letterRule = /[a-zA-Z]/;    // Pelo menos uma letra
    const numberRule = /\d/;          // Pelo menos um número

    // Verificação de requisitos
    if (lengthRule.test(password)) {
        strength += 33; // Cumpriu a regra de comprimento
        document.getElementById('length-rule').classList.remove('text-danger');
        document.getElementById('length-rule').classList.add('text-success');
    } else {
        document.getElementById('length-rule').classList.remove('text-success');
        document.getElementById('length-rule').classList.add('text-danger');
    }

    if (letterRule.test(password)) {
        strength += 33; // Cumpriu a regra de letra
        document.getElementById('letter-rule').classList.remove('text-danger');
        document.getElementById('letter-rule').classList.add('text-success');
    } else {
        document.getElementById('letter-rule').classList.remove('text-success');
        document.getElementById('letter-rule').classList.add('text-danger');
    }

    if (numberRule.test(password)) {
        strength += 34; // Cumpriu a regra de número
        document.getElementById('number-rule').classList.remove('text-danger');
        document.getElementById('number-rule').classList.add('text-success');
    } else {
        document.getElementById('number-rule').classList.remove('text-success');
        document.getElementById('number-rule').classList.add('text-danger');
    }

    // Atualiza a barra de progresso com base na força da senha
    const progressBar = document.getElementById('password-strength-bar');
    const progressText = document.getElementById('password-strength-text');
    progressBar.style.width = strength + '%';
    progressBar.setAttribute('aria-valuenow', strength);

    if (strength === 0) {
        progressText.textContent = 'Muito fraca';
    } else if (strength <= 33) {
        progressText.textContent = 'Fraca';
    } else if (strength <= 66) {
        progressText.textContent = 'Moderada';
    } else {
        progressText.textContent = 'Forte';
    }
}

// Evento para verificar a senha enquanto o usuário digita
document.getElementById('id_password1').addEventListener('input', function(event) {
    checkPasswordStrength(event.target.value);
});
