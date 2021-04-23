function utilizouHoraExtra(id){
    console.log(id);
    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;

    $.ajax({
        type: 'POST',
        url: '/registro_horas_extras/utilizou-hora-extra/'+ id + '/',
        data: {
            csrfmiddlewaretoken: token
        },
        success: function(result){
            console.log("Sucesso !!!");
            $("#mensagem").text(result.mensagem);
            $("#horas_atualizadas").text(result.horas);
        }
    });
}