var main_url = "http://10.120.0.91:8000/";

// Experiment
function startExperiment(){
	$('#main').hide();

    $.ajax({
        url: main_url + "initialize/",
        success: function(result){
            $('#experiment_id').html(result.experiment_id);
            $('#datetime').html(Date());
            $('#print').show();
        },
    }).done(function(){
        window.print();
    });
}

function finishExperiment(){
	$('#print').hide();
	$('#main').show();
}

// Rolls
function startRolls(){
	$('#main').hide();
	$('#leftRollID').val('');
	$('#rightRollID').val('');
	$('#rolls').show();
}

function logRolls(side){
	var standNumber = $('#standNumber').val();
	var rollID = $('#' + side + 'RollID').val();

	if (side == 'left') {
		message = 'Logged left roll on stand ' + standNumber + ' with ID ' + rollID + '.';
	}
	else {
		message = 'Logged right roll on stand ' + standNumber + ' with ID ' + rollID + '.';
	}

	$.ajax({
		url: main_url + "log_roll/",
		type: "POST",
		dataType: "JSON",
		data: {
			standNumber: standNumber,
			side: side,
			rollID: rollID
		},
		success: function(result){
			$('#leftRollID').val('');
			$('#rightRollID').val('');
			$('#logStatus').html(message);
		}
	});
}

function finishRolls(){
	$('#rolls').hide();
	$('#main').show();
}
