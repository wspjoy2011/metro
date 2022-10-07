
    const $webinarMainTarget = document.querySelector('.webinar-schedule-list');

    let webinarScheduleData = []
    const $webinarEventDates = [...document.querySelectorAll('.webinar-schedule-list__item')]
    const $webinarScheduleDate = document.querySelector('.webinar-schedule-date')

    let $webinarActiveItem = 0;

    for(let i = 0;  i < $webinarEventDates.length; i++) {
    const $webinarEventDateNode = $webinarEventDates[i];
    const webinarDateValue = $webinarEventDateNode.getAttribute('data-date')

    const $eventWebinars = [...$webinarEventDateNode.querySelectorAll('li[data-event]')]

    const eventWebinarsData = $eventWebinars.map((webinar) => {
    const $webinarLink = webinar.querySelector('a')
    const webinarLinkUrl = $webinarLink.getAttribute('href')
    return { title: webinar.getAttribute('data-event'), url: webinarLinkUrl }
    })

    webinarScheduleData.push({ id: (Math.random() + 1).toString(36).substring(7), date: webinarDateValue, courses: eventWebinarsData })
    webinarScheduleData = webinarScheduleData.filter((item) => item.date);
}

    $webinarMainTarget.innerHTML = '';

    for(let i = 0; i < webinarScheduleData.length; i++) {
    const webinarScheduleItem = webinarScheduleData[i]
    const webinarScheduleCourses = webinarScheduleItem.courses;

    const $webinarScheduleLi = document.createElement('li');

    const $webinarEventsList = document.createElement('ul');
    $webinarEventsList.classList.add('webinar-schedule-list-webinars');


    $webinarScheduleLi.classList.add('webinar-schedule-list__item')
    $webinarScheduleLi.style.display = 'none';


    $webinarScheduleDate.innerHTML = webinarScheduleItem.date;

    if(webinarScheduleCourses) {

    for(let j = 0; j < webinarScheduleCourses.length; j++) {
    const webinarScheduleCourse = webinarScheduleCourses[j];
    const $webinarEventsListItem = document.createElement('li');

    let counter = j + 1

    $webinarEventsListItem.innerHTML = '<span class="order-number">'+counter+'</span>'+'<a href="'+webinarScheduleCourse.url+'">'+webinarScheduleCourse.title+'</a>';

    $webinarEventsList.append($webinarEventsListItem);
}

    $webinarScheduleLi.append($webinarEventsList)

}
    if(!webinarScheduleCourses.length) {
    const noWebinarsBlock = document.createElement('li')
    noWebinarsBlock.classList.add('no-events')
    noWebinarsBlock.textContent = 'Немає вебінарів в цей день'
    $webinarEventsList.append(noWebinarsBlock)
}
    $webinarMainTarget.appendChild($webinarScheduleLi);
}

    updateWbVisibility($webinarActiveItem);




    document.querySelector('.webinar.prev-btn').addEventListener('click', function() {
    if($webinarActiveItem < 1) return false;
    $webinarActiveItem -= 1;
    [...document.querySelectorAll('.webinar-schedule-list__item')].forEach((item) => item.style.display = 'none');
    updateWbVisibility($webinarActiveItem)
})

    document.querySelector('.webinar.next-btn').addEventListener('click', function() {
    if($webinarActiveItem + 1 > webinarScheduleData.length - 1) return false;
    $webinarActiveItem += 1;
    [...document.querySelectorAll('.webinar-schedule-list__item')].forEach((item) => item.style.display = 'none');
    updateWbVisibility($webinarActiveItem)
})




    function updateWbVisibility($webinarActiveItem) {
    [...document.querySelectorAll('.webinar-schedule-list__item')][$webinarActiveItem].style.display = 'block';
    $webinarScheduleDate.textContent = webinarScheduleData[$webinarActiveItem].date
}

