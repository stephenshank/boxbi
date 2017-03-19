var main_url = "http://10.120.0.91:8000/";

function start(){
	$('#save').hide()

    $.ajax({
        url: main_url + "initialize/",
        success: function(result){
            $('#experiment_id').html(result['experiment_id'])
            $('#datetime').html(Date())
            $('#print').show()
        },
    }).done(function(){
        window.print()
    })
}

function finish(){
	$('#print').hide()
	$('#save').show()
}