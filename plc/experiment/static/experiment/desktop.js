var main_url = "http://10.120.0.91:8000/";
var experiment_id;

function retrieve(){
	$('.retrieve').hide();

    experiment_id = $('#id-input').val();

    $.ajax({
        type: "POST",
        url: main_url + "retrieve/",
        data: {
            'experiment_id': experiment_id
        },
        success: function(result){
            $('.enter').show();
            $('#datetime').html(result['start_time']);
            $('.experiment_id').html(experiment_id);
        },
        dataType: "JSON"
    })
}

function enter(){
    $('.enter').hide();

    $.ajax({
        type: "POST",
        url: main_url + "enter/",
        data: {
            experiment_id: experiment_id,
            values: _.map(_.range(10), function(num){ return $('#sample'+String(num)).val(); }),
            method: $('#method').val()
        },
        success: function(result){
            $('.retrieve').show();
            $('#result').show();
            $('#id-input').val('');
            _.each(_.range(10), function(num){ $('#sample'+String(num)).val(''); })
        },
        dataType: "JSON"
    })

}