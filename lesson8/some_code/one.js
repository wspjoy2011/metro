var timeZone = 'America/New_York'
    , dFormat = 'MM/DD/YYYY h:mm a'
    , theDate = moment.tz(moment(), timeZone).format(dFormat)
    , today = new Date(theDate)
    , todaysDate = (today.getMonth()+1)+'/'+today.getDate()+'/'+today.getFullYear()
    , firstStart = new Date(todaysDate+" 2:44:00 PM").getTime()
    , firstEnd = new Date(todaysDate+" 2:59:59 PM").getTime()
    , firstContent = "Same-day distribution orders must be received before 3 p.m. ET; otherwise, they will distribute the next business day."+'<br><br>Time until 3 p.m ET: <span id="dailyCdTimer"></span>'
    , secondStart = new Date(todaysDate+" 11:44:00 PM").getTime()
    , secondEnd = new Date(todaysDate+" 11:59:59 PM").getTime()
    , secondContent = "Orders for distribution next-business day must be received before midnight ET; otherwise, an additional same-day distribution fee will be assessed."+'<br><br>Time until midnight ET: <span id="dailyCdTimer"></span>'
    , timeStart = ""
    , timeEnd = ""
    , timeNow = new Date(theDate).getTime()
    , pauseTime = 180000 // 3 minutes
    , interval = null
    , offsetMillis = 0
    , dialogTitle = "Daily Distribution Cutoff Notification"
    , firstBlockedDay = ""
    , secondBlockedDay = "";

//alert("Eastern Time Is: "+theDate);

if (timeNow < firstStart || (timeNow >= firstStart && timeNow <= firstEnd)){
    timeStart = firstStart;
    timeEnd = firstEnd;
    firstBlockedDay = 6 // block saturday for 5pm trigger
    secondBlockedDay = 0; // block sunday for 5pm trigger
} else if ((timeNow > firstEnd && timeNow < secondStart) || (timeNow >= secondStart && timeNow <= secondEnd)) {
    timeStart = secondStart;
    timeEnd = secondEnd;
    firstBlockedDay = 5; // block friday for midnight trigger
    secondBlockedDay = 6; // block saturday for midnight trigger
}

if (timeStart !== "" && timeEnd !== "" && firstBlockedDay !== "" && secondBlockedDay !== "" && (today.getDay() != firstBlockedDay && today.getDay() != secondBlockedDay)){
    // don't keep time if the day is blocked for this time spot
    offsetMillis = timeStart - timeNow;
    if (timeNow < timeStart){
        setTimeout(keepTime, offsetMillis);
    } else if (timeNow >= timeStart && timeNow <= timeEnd){
        keepTime();
    }
}

var dailyCdTimer = setInterval(function() {

    var rightNow = moment.tz(moment(), timeZone).format('MM/DD/YYYY h:mm:ss a');
    var now = new Date(rightNow).getTime();
    var distance = timeEnd - now;

    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);

    if (distance <= 0 || (minutes <= 0 && seconds <= 0)) {
        $("#dailyCdTimer").text("");
        clearInterval(dailyCdTimer);
    } else {
        $("#dailyCdTimer").text(minutes + "m " + seconds + "s ");
    }
}, 1000);

function keepTime(){
    popNotice();
    Tinterval = setInterval(alertTimeTrigger, pauseTime);
}

function alertTimeTrigger() {
    var cDate = moment.tz(moment(), timeZone).format(dFormat);
    curTime = new Date(cDate).getTime();
    if (curTime >= timeEnd){
        clearInterval(Tinterval);
    } else {
        popNotice();
    }
}

function popNotice(){
    $(function() {
        var useNotification = firstContent,
            curtime = new Date(theDate).getTime();
        if (curtime >= firstEnd){
            useNotification = secondContent;
        }
        $("#dailyNotification").html(useNotification);
        $("#dailyNotification").dialog({
            buttons: [{
                text: "OK",
                click: function () {
                    $("#dailyNotification").dialog('destroy').empty();
                }
            }],
            closeOnEscape: false,
            modal: true,
            title: dialogTitle,
            open: function () {
                $(this).closest('.ui-dialog').find('.ui-dialog-titlebar-close').hide();
            }
        });
    });
}