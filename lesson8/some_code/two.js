const DATEPICKER = '#datepicker';

const SERVER_DATE = (function() {
    let timeZone = 'America/New_York',
        dateFormat = 'MM/DD/YYYY',
        dateTimeFormat = 'MM/DD/YYYY h:mm a',
        currentDate = moment.tz(moment(), timeZone),
        currentDateString = currentDate.format(dateFormat),
        currentDateTimeString = currentDate.format(dateTimeFormat),
        currentDateTimestamp = currentDate.utc(true).valueOf();

    // set and configure 3pm notification
    let beforeThreePmNotification = {
        displayBetween: {
            start: `${currentDateString} 2:44:00 PM`,
            startTimestamp: moment(`${currentDateString} 2:44:00 PM`).utc(true).valueOf(),
            end: `${currentDateString} 2:59:59 PM`,
            endTimestamp: moment(`${currentDateString} 2:59:59 PM`).utc(true).valueOf()
        },
        title: 'Daily Distribution Cutoff Notification',
        text: `Same-day distribution orders must be received before 3 p.m. ET; otherwise, they will distribute the next business day.
               <br><br>
               Time until 3 p.m ET: <span id="dailyCdTimer"></span>
               `,
        needToDisplay: false
    }
    beforeThreePmNotification.needToDisplay = (
        currentDateTimestamp >= beforeThreePmNotification.displayBetween.startTimestamp
        && currentDateTimestamp <= beforeThreePmNotification.displayBetween.endTimestamp
    )

    // set and configure midnight notification
    let beforeMidnightNotification = {
        displayBetween: {
            start: `${currentDateString} 11:44:00 PM`,
            startTimestamp: moment(`${currentDateString} 11:44:00 PM`).utc(true).valueOf(),
            end: `${currentDateString} 11:59:59 PM`,
            endTimestamp: moment(`${currentDateString} 11:59:59 PM`).utc(true).valueOf()
        },
        title: 'Daily Distribution Cutoff Notification',
        text: `Orders for distribution next-business day must be received before midnight ET; otherwise, an additional same-day distribution fee will be assessed.
               <br><br>
               Time until midnight ET: <span id="dailyCdTimer"></span>
               `,
        needToDisplay: false
    }
    beforeMidnightNotification.needToDisplay = (
        currentDateTimestamp >= beforeMidnightNotification.displayBetween.startTimestamp
        && currentDateTimestamp <= beforeMidnightNotification.displayBetween.endTimestamp
    )

    return {
        timeZone,
        dateFormat,
        dateTimeFormat,
        currentDate,
        currentDateString,
        currentDateTimeString,
        currentDateTimestamp,
        beforeThreePmNotification,
        beforeMidnightNotification
    }
})();

// init timers
window.addEventListener('load', function () {
    // before 3pm notification
    if (SERVER_DATE.beforeThreePmNotification.needToDisplay){
        const timer  = new Timer('#dailyNotification', {
            title: SERVER_DATE.beforeThreePmNotification.title,
            text: SERVER_DATE.beforeThreePmNotification.text,
            tick: SERVER_DATE.beforeThreePmNotification.displayBetween.endTimestamp - SERVER_DATE.currentDateTimestamp,
            minPickerDate: '+1'
        })
    }

    // before midnight notification
    if (SERVER_DATE.beforeMidnightNotification.needToDisplay){
        const timer  = new Timer('#dailyNotification', {
            title: SERVER_DATE.beforeMidnightNotification.title,
            text: SERVER_DATE.beforeMidnightNotification.text,
            tick: SERVER_DATE.beforeMidnightNotification.displayBetween.endTimestamp - SERVER_DATE.currentDateTimestamp
        })
    }
})

/**
 * Create Timer
 * @param nodeId
 * @param {Object} options
 * @param {string} options.title Dialog title
 * @param {string} options.text Dialog text
 * @param {number} options.tick Time for timer in milliseconds
 * @param {string} options.minPickerDate Min selectable datepicker date
 * @returns {{resume: createInterval, pause: pause}}
 * @constructor
 */
function Timer(nodeId, options) {
    if (!options.tick) return;

    $(nodeId).html(options.text);
    $(nodeId).dialog({
        buttons: [{
            text: "OK",
            click: function () {
                $(nodeId).dialog('destroy').empty();
            }
        }],
        closeOnEscape: false,
        modal: true,
        title: options.title,
        open: function () {
            $(this).closest('.ui-dialog').find('.ui-dialog-titlebar-close').hide();
        }
    });

    let leftTickTime = options.tick;
    let tickInterval;

    function createInterval() {
        tickInterval = setInterval(function () {
            leftTickTime -= 1000;
            let minutes = Math.floor((leftTickTime % (1000 * 60 * 60)) / (1000 * 60)),
                seconds = Math.floor((leftTickTime % (1000 * 60)) / 1000);

            if (leftTickTime < 0) {
                $("#dailyCdTimer").text("");
                clearInterval(tickInterval);
                if (options.minPickerDate) {
                    $(DATEPICKER).datepicker('option', 'minDate', options.minPickerDate);
                }
                return;
            }
            $("#dailyCdTimer").text(minutes + "m " + seconds + "s ");
        }, 1000);
    }

    createInterval(); // first time init interval
    return {
        pause: function () {
            clearInterval(tickInterval)
        },
        resume: createInterval
    }
}