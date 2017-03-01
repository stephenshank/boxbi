$(document).ready(function(){
    
    
    $( "#recipeCardNavToStackerPage" ).click(function () {
            window.location.href = 'index.html'
        });
    
     $( "#loadRecipeButton" ).click(function () {
            console.log("LOAD Clicked");
        });
     
      $( "#saveRecipeButton" ).click(function () {
            console.log("SAVE Clicked");
            console.log("Roll#1-"+$("#roll_1").val()+" Roll#2-"+$("#roll_2").val()+" Roll#3-"+$("#roll_3").val()+" Roll#4-"+$("#roll_4").val()+" Roll#5-"+$("#roll_5").val());
        });
        
        
        
    $(window).on("load", function() {
        
   //var intervalID = window.setInterval(getNewPLCData, 1000);
    
    
    
    $("#recipeCardBase").css("background-image","url('static/img/recipeCardBase.png')");
    $("#recipeCardBase").css("z-index", "1");
    
    $("#recipeCardMoistSFTOPDial").css("background-image","url('static/img/heatMoistDial.png')");
    $("#recipeCardMoistSFTOPDial").css("z-index", "2");
    
    $("#recipeCardMoistDBBOTDial").css("background-image","url('static/img/heatMoistDial.png')");
    $("#recipeCardMoistDBBOTDial").css("z-index", "2");
    
    $("#recipeCardHeatSFTOPDial").css("background-image","url('static/img/heatMoistDial.png')");
    $("#recipeCardHeatSFTOPDial").css("z-index", "2");
    
    $("#recipeCardHeatDBBOTDial").css("background-image","url('static/img/heatMoistDial.png')");
    $("#recipeCardHeatDBBOTDial").css("z-index", "2");
    
    $("#recipeCardMachineSpeedDial").css("background-image","url('static/img/heatMoistDial.png')");
    $("#recipeCardMachineSpeedDial").css("z-index", "2");
    
        
    function scaleTheSheet(divTagID,cssVarName,localVarName) {
        if ($("#baseBG").height()/1080<=$("#baseBG").width()/1920) {
            $("#"+divTagID).css(cssVarName,($("#baseBG").height()/1080)*localVarName);
        }else{
            $("#"+divTagID).css(cssVarName,($("#baseBG").width()/1920)*localVarName);
        }
    }
    
    function scaleTheSheetByClass(divTagID,cssVarName,localVarName) {
        if ($("#baseBG").height()/1080<=$("#baseBG").width()/1920) {
            $("."+divTagID).css(cssVarName,($("#baseBG").height()/1080)*localVarName);
        }else{
            $("."+divTagID).css(cssVarName,($("#baseBG").width()/1920)*localVarName);
        }
    }
    
    function populateTheHTMLDivs() {
       
        scaleTheSheet("recipeCardClock","height",30);
        scaleTheSheet("recipeCardClock","width",650);
        scaleTheSheet("recipeCardClock","font-size",15);
        
        scaleTheSheet("recipeCardNavToStackerPage","height",50);
        scaleTheSheet("recipeCardNavToStackerPage","width",250);
        scaleTheSheet("recipeCardNavToStackerPage","left",1650);
        scaleTheSheet("recipeCardNavToStackerPage","font-size",25);
        
        scaleTheSheet("recipeCardLabelHeader","height",50);
        scaleTheSheet("recipeCardLabelHeader","width",1920);
        scaleTheSheet("recipeCardLabelHeader","font-size",66);    
        
        scaleTheSheet("recipeCardHotPlate1OutterUP","height",40);
        scaleTheSheet("recipeCardHotPlate1OutterUP","width",100);
        scaleTheSheet("recipeCardHotPlate1OutterUP","left",537);
        scaleTheSheet("recipeCardHotPlate1OutterUP","top",505);
        scaleTheSheet("recipeCardHotPlate1OutterUP","font-size",35);
        
        scaleTheSheet("recipeCardHotPlate1OutterDOWN","height",40);
        scaleTheSheet("recipeCardHotPlate1OutterDOWN","width",100);
        scaleTheSheet("recipeCardHotPlate1OutterDOWN","left",537);
        scaleTheSheet("recipeCardHotPlate1OutterDOWN","top",550);
        scaleTheSheet("recipeCardHotPlate1OutterDOWN","font-size",35);
        
        scaleTheSheet("recipeCardHotPlate2OutterUP","height",40);
        scaleTheSheet("recipeCardHotPlate2OutterUP","width",100);
        scaleTheSheet("recipeCardHotPlate2OutterUP","left",642);
        scaleTheSheet("recipeCardHotPlate2OutterUP","top",505);
        scaleTheSheet("recipeCardHotPlate2OutterUP","font-size",35);
        
        scaleTheSheet("recipeCardHotPlate2OutterDOWN","height",40);
        scaleTheSheet("recipeCardHotPlate2OutterDOWN","width",100);
        scaleTheSheet("recipeCardHotPlate2OutterDOWN","left",642);
        scaleTheSheet("recipeCardHotPlate2OutterDOWN","top",550);
        scaleTheSheet("recipeCardHotPlate2OutterDOWN","font-size",35);
        
        scaleTheSheet("recipeCardHotPlate3OutterUP","height",40);
        scaleTheSheet("recipeCardHotPlate3OutterUP","width",100);
        scaleTheSheet("recipeCardHotPlate3OutterUP","left",746);
        scaleTheSheet("recipeCardHotPlate3OutterUP","top",505);
        scaleTheSheet("recipeCardHotPlate3OutterUP","font-size",35);
        
        scaleTheSheet("recipeCardHotPlate3OutterDOWN","height",40);
        scaleTheSheet("recipeCardHotPlate3OutterDOWN","width",100);
        scaleTheSheet("recipeCardHotPlate3OutterDOWN","left",746);
        scaleTheSheet("recipeCardHotPlate3OutterDOWN","top",550);
        scaleTheSheet("recipeCardHotPlate3OutterDOWN","font-size",35);
        
        scaleTheSheet("recipeCardHotPlate4OutterUP","height",40);
        scaleTheSheet("recipeCardHotPlate4OutterUP","width",100);
        scaleTheSheet("recipeCardHotPlate4OutterUP","left",850);
        scaleTheSheet("recipeCardHotPlate4OutterUP","top",505);
        scaleTheSheet("recipeCardHotPlate4OutterUP","font-size",35);
        
        scaleTheSheet("recipeCardHotPlate4OutterDOWN","height",40);
        scaleTheSheet("recipeCardHotPlate4OutterDOWN","width",100);
        scaleTheSheet("recipeCardHotPlate4OutterDOWN","left",850);
        scaleTheSheet("recipeCardHotPlate4OutterDOWN","top",550);
        scaleTheSheet("recipeCardHotPlate4OutterDOWN","font-size",35);
        
        scaleTheSheet("recipeCardHotPlate5OutterUP","height",40);
        scaleTheSheet("recipeCardHotPlate5OutterUP","width",100);
        scaleTheSheet("recipeCardHotPlate5OutterUP","left",955);
        scaleTheSheet("recipeCardHotPlate5OutterUP","top",505);
        scaleTheSheet("recipeCardHotPlate5OutterUP","font-size",35);
        
        scaleTheSheet("recipeCardHotPlate5OutterDOWN","height",40);
        scaleTheSheet("recipeCardHotPlate5OutterDOWN","width",100);
        scaleTheSheet("recipeCardHotPlate5OutterDOWN","left",955);
        scaleTheSheet("recipeCardHotPlate5OutterDOWN","top",550);
        scaleTheSheet("recipeCardHotPlate5OutterDOWN","font-size",35);
        
        scaleTheSheet("recipeCardHotPlate6OutterUP","height",40);
        scaleTheSheet("recipeCardHotPlate6OutterUP","width",100);
        scaleTheSheet("recipeCardHotPlate6OutterUP","left",537);
        scaleTheSheet("recipeCardHotPlate6OutterUP","top",599);
        scaleTheSheet("recipeCardHotPlate6OutterUP","font-size",35);
        
        scaleTheSheet("recipeCardHotPlate6OutterDOWN","height",40);
        scaleTheSheet("recipeCardHotPlate6OutterDOWN","width",100);
        scaleTheSheet("recipeCardHotPlate6OutterDOWN","left",537);
        scaleTheSheet("recipeCardHotPlate6OutterDOWN","top",645);
        scaleTheSheet("recipeCardHotPlate6OutterDOWN","font-size",35);
        
        scaleTheSheet("recipeCardHotPlate7OutterUP","height",40);
        scaleTheSheet("recipeCardHotPlate7OutterUP","width",100);
        scaleTheSheet("recipeCardHotPlate7OutterUP","left",642);
        scaleTheSheet("recipeCardHotPlate7OutterUP","top",599);
        scaleTheSheet("recipeCardHotPlate7OutterUP","font-size",35);
        
        scaleTheSheet("recipeCardHotPlate7OutterDOWN","height",40);
        scaleTheSheet("recipeCardHotPlate7OutterDOWN","width",100);
        scaleTheSheet("recipeCardHotPlate7OutterDOWN","left",642);
        scaleTheSheet("recipeCardHotPlate7OutterDOWN","top",645);
        scaleTheSheet("recipeCardHotPlate7OutterDOWN","font-size",35);
        
        scaleTheSheet("recipeCardHotPlate8OutterUP","height",40);
        scaleTheSheet("recipeCardHotPlate8OutterUP","width",100);
        scaleTheSheet("recipeCardHotPlate8OutterUP","left",746);
        scaleTheSheet("recipeCardHotPlate8OutterUP","top",599);
        scaleTheSheet("recipeCardHotPlate8OutterUP","font-size",35);
        
        scaleTheSheet("recipeCardHotPlate8OutterDOWN","height",40);
        scaleTheSheet("recipeCardHotPlate8OutterDOWN","width",100);
        scaleTheSheet("recipeCardHotPlate8OutterDOWN","left",746);
        scaleTheSheet("recipeCardHotPlate8OutterDOWN","top",645);
        scaleTheSheet("recipeCardHotPlate8OutterDOWN","font-size",35);
        
        scaleTheSheet("recipeCardHotPlate9OutterUP","height",40);
        scaleTheSheet("recipeCardHotPlate9OutterUP","width",100);
        scaleTheSheet("recipeCardHotPlate9OutterUP","left",850);
        scaleTheSheet("recipeCardHotPlate9OutterUP","top",599);
        scaleTheSheet("recipeCardHotPlate9OutterUP","font-size",35);
        
        scaleTheSheet("recipeCardHotPlate9OutterDOWN","height",40);
        scaleTheSheet("recipeCardHotPlate9OutterDOWN","width",100);
        scaleTheSheet("recipeCardHotPlate9OutterDOWN","left",850);
        scaleTheSheet("recipeCardHotPlate9OutterDOWN","top",645);
        scaleTheSheet("recipeCardHotPlate9OutterDOWN","font-size",35);
        
        scaleTheSheet("recipeCardHotPlate10OutterUP","height",40);
        scaleTheSheet("recipeCardHotPlate10OutterUP","width",100);
        scaleTheSheet("recipeCardHotPlate10OutterUP","left",955);
        scaleTheSheet("recipeCardHotPlate10OutterUP","top",599);
        scaleTheSheet("recipeCardHotPlate10OutterUP","font-size",35);
        
        scaleTheSheet("recipeCardHotPlate10OutterDOWN","height",40);
        scaleTheSheet("recipeCardHotPlate10OutterDOWN","width",100);
        scaleTheSheet("recipeCardHotPlate10OutterDOWN","left",955);
        scaleTheSheet("recipeCardHotPlate10OutterDOWN","top",645);
        scaleTheSheet("recipeCardHotPlate10OutterDOWN","font-size",35);
        
        scaleTheSheet("recipeCardRSInfo","height",246);
        scaleTheSheet("recipeCardRSInfo","width",270);
        scaleTheSheet("recipeCardRSInfo","left",295);
        scaleTheSheet("recipeCardRSInfo","top",155);
        scaleTheSheet("recipeCardRSInfo","font-size",25);
        
        scaleTheSheet("recipeCardRSLabel","height",246);
        scaleTheSheet("recipeCardRSLabel","width",260);
        scaleTheSheet("recipeCardRSLabel","left",30);
        scaleTheSheet("recipeCardRSLabel","top",155);
        scaleTheSheet("recipeCardRSLabel","font-size",25);
        
        scaleTheSheet("recipeCardBFluteSFInfo","height",246);
        scaleTheSheet("recipeCardBFluteSFInfo","width",220);
        scaleTheSheet("recipeCardBFluteSFInfo","left",820);
        scaleTheSheet("recipeCardBFluteSFInfo","top",155);
        scaleTheSheet("recipeCardBFluteSFInfo","font-size",25);
        
        scaleTheSheet("recipeCardCEFLuteSFInfo","height",246);
        scaleTheSheet("recipeCardCEFLuteSFInfo","width",220);
        scaleTheSheet("recipeCardCEFLuteSFInfo","left",1287);
        scaleTheSheet("recipeCardCEFLuteSFInfo","top",155);
        scaleTheSheet("recipeCardCEFLuteSFInfo","font-size",25);
        
        scaleTheSheet("recipeCardTripleStackPHInfo","height",246);
        scaleTheSheet("recipeCardTripleStackPHInfo","width",220);
        scaleTheSheet("recipeCardTripleStackPHInfo","left",1660);
        scaleTheSheet("recipeCardTripleStackPHInfo","top",155);
        scaleTheSheet("recipeCardTripleStackPHInfo","font-size",17);
        
        scaleTheSheet("recipeCardDBGlueStationInfo","height",246);
        scaleTheSheet("recipeCardDBGlueStationInfo","width",296);
        scaleTheSheet("recipeCardDBGlueStationInfo","left",180);
        scaleTheSheet("recipeCardDBGlueStationInfo","top",450);
        scaleTheSheet("recipeCardDBGlueStationInfo","font-size",20);
        
        scaleTheSheet("recipeCardMoistSFTOP","height",50);
        scaleTheSheet("recipeCardMoistSFTOP","width",315);
        scaleTheSheet("recipeCardMoistSFTOP","left",210);
        scaleTheSheet("recipeCardMoistSFTOP","top",800);
        scaleTheSheet("recipeCardMoistSFTOP","font-size",25);
        
        scaleTheSheet("recipeCardMoistSFTOPDial","height",25);
        scaleTheSheet("recipeCardMoistSFTOPDial","width",100);
        scaleTheSheet("recipeCardMoistSFTOPDial","left",70);
        scaleTheSheet("recipeCardMoistSFTOPDial","top",825);
        $("#recipeCardMoistSFTOPDial").css("transform","rotateZ(0deg)");
        
        scaleTheSheet("recipeCardMoistDBBOT","height",50);
        scaleTheSheet("recipeCardMoistDBBOT","width",315);
        scaleTheSheet("recipeCardMoistDBBOT","left",30);
        scaleTheSheet("recipeCardMoistDBBOT","top",935);
        scaleTheSheet("recipeCardMoistDBBOT","font-size",25);
        
        scaleTheSheet("recipeCardMoistDBBOTDial","height",25);
        scaleTheSheet("recipeCardMoistDBBOTDial","width",100);
        scaleTheSheet("recipeCardMoistDBBOTDial","left",383);
        scaleTheSheet("recipeCardMoistDBBOTDial","top",950);
        $("#recipeCardMoistDBBOTDial").css("transform","rotateZ(0deg)");
        
        scaleTheSheet("recipeCardHeatSFTOP","height",50);
        scaleTheSheet("recipeCardHeatSFTOP","width",315);
        scaleTheSheet("recipeCardHeatSFTOP","left",750);
        scaleTheSheet("recipeCardHeatSFTOP","top",800);
        scaleTheSheet("recipeCardHeatSFTOP","font-size",20);
        
        scaleTheSheet("recipeCardHeatSFTOPDial","height",25);
        scaleTheSheet("recipeCardHeatSFTOPDial","width",100);
        scaleTheSheet("recipeCardHeatSFTOPDial","left",608);
        scaleTheSheet("recipeCardHeatSFTOPDial","top",825);
        $("#recipeCardHeatSFTOPDial").css("transform","rotateZ(0deg)");
    
        
        scaleTheSheet("recipeCardHeatDBBOT","height",50);
        scaleTheSheet("recipeCardHeatDBBOT","width",315);
        scaleTheSheet("recipeCardHeatDBBOT","left",570);
        scaleTheSheet("recipeCardHeatDBBOT","top",935);
        scaleTheSheet("recipeCardHeatDBBOT","font-size",20);
        
        scaleTheSheet("recipeCardHeatDBBOTDial","height",25);
        scaleTheSheet("recipeCardHeatDBBOTDial","width",100);
        scaleTheSheet("recipeCardHeatDBBOTDial","left",925);
        scaleTheSheet("recipeCardHeatDBBOTDial","top",950);
        $("#recipeCardHeatDBBOTDial").css("transform","rotateZ(0deg)");
        
        
        scaleTheSheet("recipeCardMachineSpeed","height",100);
        scaleTheSheet("recipeCardMachineSpeed","width",200);
        scaleTheSheet("recipeCardMachineSpeed","left",1510);
        scaleTheSheet("recipeCardMachineSpeed","top",720);
        scaleTheSheet("recipeCardMachineSpeed","font-size",100);
        
        scaleTheSheet("recipeCardMachineSpeedDial","height",50);
        scaleTheSheet("recipeCardMachineSpeedDial","width",200);
        scaleTheSheet("recipeCardMachineSpeedDial","left",1508);
        scaleTheSheet("recipeCardMachineSpeedDial","top",660);
        $("#recipeCardMachineSpeedDial").css("transform","rotateZ(0deg)");
        
        
        scaleTheSheet("recipeCardOrderData","height",600);
        scaleTheSheet("recipeCardOrderData","width",320);
        scaleTheSheet("recipeCardOrderData","left",1110);
        scaleTheSheet("recipeCardOrderData","top",450);
        scaleTheSheet("recipeCardOrderData","font-size",25);
        
        scaleTheSheet("recipeCardScore","height",60);
        scaleTheSheet("recipeCardScore","width",230);
        scaleTheSheet("recipeCardScore","left",1660);
        scaleTheSheet("recipeCardScore","top",450);
        scaleTheSheet("recipeCardScore","font-size",40);
        

        scaleTheSheet("loadRecipeButton","width",200);
        scaleTheSheet("loadRecipeButton","left",1460);
        scaleTheSheet("loadRecipeButton","top",950);
        scaleTheSheet("loadRecipeButton","font-size",60);
        
        scaleTheSheet("saveRecipeButton","width",200);
        scaleTheSheet("saveRecipeButton","left",1680);
        scaleTheSheet("saveRecipeButton","top",950);
        scaleTheSheet("saveRecipeButton","font-size",60);
        
        scaleTheSheetByClass("rollInputTextBox","width",250);
        scaleTheSheetByClass("rollInputTextBox","height",20);
        
        
        
    
    }
    populateTheHTMLDivs();
    
    $( window ).resize(function() {
        populateTheHTMLDivs(); 
    });
    
    
    function getNewPLCData() {
        
        
        var topMoistDialMinMovement = 0;
        var topMoistDialMaxMovement = 170;
        var topMoistDialMinValue = 4;
        var topMoistDialMaxValue = 12;
        
        var botMoistDialMinMovement = 0;
        var botMoistDialMaxMovement = 170;
        var botMoistDialMinValue = 4;
        var botMoistDialMaxValue = 12;
        
        var topTempDialMinMovement = 0;
        var topTempDialMaxMovement = 170;
        var topTempDialMinValue = 40;
        var topTempDialMaxValue = 250;
        
        var botTempDialMinMovement = 0;
        var botTempDialMaxMovement = 170;
        var botTempDialMinValue = 40;
        var botTempDialMaxValue = 250;
        
        var machineSpeedMinMovement = 0;
        var machineSpeedMaxMovement = 170;
        var machineSpeedMinValue = 0;
        var machineSpeedMaxValue = 1000;
        
        
        
    $.ajax({
        type: "GET",
        url: "http://10.120.0.91:8000/plc/?format=json"
    })
    .done(function( data ) {
        console.log("Completed an AJAX call");
        console.log(data);
        var tempValuePlaceHolder = "#NULL#";
        
        $("#recipeCardClock").text(new Date());
        
        var obj = $("#recipeCardRSLabel").text("--B Flute-Liner Roll #: \n ~B Flute-MED Roll #: \n --C/E Flute-Liner Roll #: \n ~C/E Flute-MED Roll #: \n --DB-Liner Roll #: \n \n \n Basis Weight:");
        obj.html(obj.html().replace(/\n/g,'<br/>'));
        
        //var obj2 = $("#recipeCardRSInfo").text(""+tempValuePlaceHolder+" \n "+tempValuePlaceHolder+" \n "+tempValuePlaceHolder+" \n "+tempValuePlaceHolder+" \n "+tempValuePlaceHolder+" \n \n \n "+tempValuePlaceHolder+"/"+tempValuePlaceHolder+"/"+tempValuePlaceHolder+"");
        //obj2.html(obj2.html().replace(/\n/g,'<br/>'));
        
        var obj3 = $("#recipeCardBFluteSFInfo").text("B Flute-SF\n Glue Gap: "+tempValuePlaceHolder+"\n Viscosity: "+tempValuePlaceHolder+" SEC\n Temp: "+tempValuePlaceHolder+" F");
        obj3.html(obj3.html().replace(/\n/g,'<br/>'));
        
        var obj4 = $("#recipeCardCEFLuteSFInfo").text("C/E Flute-SF\n Glue Gap: "+tempValuePlaceHolder+"\n Viscosity: "+tempValuePlaceHolder+" SEC\n Temp: "+tempValuePlaceHolder+" F");
        obj4.html(obj4.html().replace(/\n/g,'<br/>'));
        
        var obj5 = $("#recipeCardTripleStackPHInfo").text("Top\n Wrap: " +(data.UTSPWrapPercentage)+"%\n Temp: OP-"+(data.TempLinerUpOpBefGM)+"/DR-"+(data.TempLinerUpDrBefGM)+" F\n\n Mid\n Wrap: " +(data.MTSPWrapPercentage)+"%\n Temp: "+tempValuePlaceHolder+" F\n\n Bot\n Wrap: " +(data.LTSPWrapPercentage)+"%\n Temp: "+tempValuePlaceHolder+" F");
        obj5.html(obj5.html().replace(/\n/g,'<br/>'));
        
        var obj6 = $("#recipeCardDBGlueStationInfo").text("Top Glue Station\n Glue Gap: "+(data.UpperMeterRollGap).toFixed(3)+"\n Viscosity: "+tempValuePlaceHolder+" SEC\n Temp: "+tempValuePlaceHolder+" F\n\n Bot Glue Station\n Glue Gap: "+(data.LowerMeterRollGap).toFixed(3)+"\n Viscosity: "+tempValuePlaceHolder+" SEC\n Temp: OP-"+(data.TempLinerLowOpBefHP)+" F/DR-"+(data.TempLinerLowDrBefHP)+" F");
        obj6.html(obj6.html().replace(/\n/g,'<br/>'));
        
        $("#recipeCardMoistSFTOP").text("SF-TOP Moisture: "+(data.TopMoisture2).toFixed(2)+" %");
        $("#recipeCardMoistSFTOPDial").css("transform","rotateZ("+(topMoistDialMaxMovement/topMoistDialMaxValue)*(data.TopMoisture2).toFixed(2)+"deg)");
        $("#recipeCardMoistDBBOT").text("DB-BOT Moisture: "+(data.BottomMoisture2).toFixed(2)+" %");
        $("#recipeCardMoistDBBOTDial").css("transform","rotateZ("+(botMoistDialMaxMovement/botMoistDialMaxValue)*(data.BottomMoisture2).toFixed(2)+"deg)");
        
        $("#recipeCardHeatSFTOP").text("SF-TOP Temp: OP-"+(data.TempUpOpAS)+"/DR-"+(data.TempUpDrAS)+" F");
        $("#recipeCardHeatSFTOPDial").css("transform","rotateZ("+(topTempDialMaxMovement/topTempDialMaxValue)*(((data.TempUpOpAS)+(data.TempUpDrAS))/2)+"deg)");
        $("#recipeCardHeatDBBOT").text("DB-BOT Temp: OP-"+(data.TempLowOpAS)+"/DR-"+(data.TempLowDrAS)+" F");
        $("#recipeCardHeatDBBOTDial").css("transform","rotateZ("+(botTempDialMaxMovement/botTempDialMaxValue)*(((data.TempLowOpAS)+(data.TempLowDrAS))/2)+"deg)");
        
        $("#recipeCardMachineSpeed").text((data.MachineSpeed));
        $("#recipeCardMachineSpeedDial").css("transform","rotateZ("+(machineSpeedMaxMovement/machineSpeedMaxValue)*(data.MachineSpeed)+"deg)");
        var obj7 = $("#recipeCardOrderData").text("Top Order#: "+tempValuePlaceHolder+"\n Customer: "+tempValuePlaceHolder+"\n QTY: "+tempValuePlaceHolder+" of "+tempValuePlaceHolder+"\n\n Bot Order#: "+tempValuePlaceHolder+"\n Customer: "+tempValuePlaceHolder+"\n QTY: "+tempValuePlaceHolder+" of "+tempValuePlaceHolder+"");
        obj7.html(obj7.html().replace(/\n/g,'<br/>'));
        $("#recipeCardScore").text("Score: 000");
        
       
        if (data.Shoe1 == 0) {
            //Down
            $("#recipeCardHotPlate1OutterUP").hide();
            $("#recipeCardHotPlate1OutterDOWN").show();
        }else{
            //UP
            $("#recipeCardHotPlate1OutterUP").show();
            $("#recipeCardHotPlate1OutterDOWN").hide();
        }
        if (data.Shoe2 == 0) {
            //Down
            $("#recipeCardHotPlate2OutterUP").hide();
            $("#recipeCardHotPlate2OutterDOWN").show();
        }else{
            //UP
            $("#recipeCardHotPlate2OutterUP").show();
            $("#recipeCardHotPlate2OutterDOWN").hide();
        }
        if (data.Shoe3 == 0) {
            //Down
            $("#recipeCardHotPlate3OutterUP").hide();
            $("#recipeCardHotPlate3OutterDOWN").show();
        }else{
            //UP
            $("#recipeCardHotPlate3OutterUP").show();
            $("#recipeCardHotPlate3OutterDOWN").hide();
        }
        if (data.Shoe4 == 0) {
            //Down
            $("#recipeCardHotPlate4OutterUP").hide();
            $("#recipeCardHotPlate4OutterDOWN").show();
        }else{
            //UP
            $("#recipeCardHotPlate4OutterUP").show();
            $("#recipeCardHotPlate4OutterDOWN").hide();
        }if (data.Shoe5 == 0) {
            //Down
            $("#recipeCardHotPlate5OutterUP").hide();
            $("#recipeCardHotPlate5OutterDOWN").show();
        }else{
            //UP
            $("#recipeCardHotPlate5OutterUP").show();
            $("#recipeCardHotPlate5OutterDOWN").hide();
        }if (data.Shoe6 == 0) {
            //Down
            $("#recipeCardHotPlate6OutterUP").hide();
            $("#recipeCardHotPlate6OutterDOWN").show();
        }else{
            //UP
            $("#recipeCardHotPlate6OutterUP").show();
            $("#recipeCardHotPlate6OutterDOWN").hide();
        }if (data.Shoe7 == 0) {
            //Down
            $("#recipeCardHotPlate7OutterUP").hide();
            $("#recipeCardHotPlate7OutterDOWN").show();
        }else{
            //UP
            $("#recipeCardHotPlate7OutterUP").show();
            $("#recipeCardHotPlate7OutterDOWN").hide();
        }if (data.Shoe8 == 0) {
            //Down
            $("#recipeCardHotPlate8OutterUP").hide();
            $("#recipeCardHotPlate8OutterDOWN").show();
        }else{
            //UP
            $("#recipeCardHotPlate8OutterUP").show();
            $("#recipeCardHotPlate8OutterDOWN").hide();
        }if (data.Shoe9 == 0) {
            //Down
            $("#recipeCardHotPlate9OutterUP").hide();
            $("#recipeCardHotPlate9OutterDOWN").show();
        }else{
            //UP
            $("#recipeCardHotPlate9OutterUP").show();
            $("#recipeCardHotPlate9OutterDOWN").hide();
        }if (data.Shoe10 == 0) {
            //Down
            $("#recipeCardHotPlate10OutterUP").hide();
            $("#recipeCardHotPlate10OutterDOWN").show();
        }else{
            //UP
            $("#recipeCardHotPlate10OutterUP").show();
            $("#recipeCardHotPlate10OutterDOWN").hide();
        }
        
      setTimeout(function (){

  // Something you want delayed.
  getNewPLCData();

}, 5000); // How long do you want the delay to be (in milliseconds)?   
   
    })
    .fail(function(error) {
        console.log("Error");
        console.log( error );
        clearInterval(intervalID);
    });
    
    
    }
   
    
       

   
    getNewPLCData();
    

    
    
    
    })

});    