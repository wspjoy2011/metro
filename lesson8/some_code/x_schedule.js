


const $mainTarget = document.querySelector('.week-schedule-list');

let weekScheduleData = []
const $eventDates = [...document.querySelectorAll('.week-schedule-list__item')]
const $weekScheduleDate = document.querySelector('.week-schedule-date')

let activeItem = 0;

for(let i = 0; i < $eventDates.length; i++) {
    const $eventDateNode = $eventDates[i];
    const eventDateValue = $eventDateNode.getAttribute('data-date')


    const $eventCourses = [...$eventDateNode.querySelectorAll('li[data-event]')]

    const eventCoursesData = $eventCourses.map((course) => {
        const $courseLink = course.querySelector('a')
        const courseLinkUrl = $courseLink.getAttribute('href')
        return { title: course.getAttribute('data-event'), url: courseLinkUrl }
    })

    weekScheduleData.push({ id: (Math.random() + 1).toString(36).substring(7), date: eventDateValue, courses: eventCoursesData })
}

weekScheduleData = weekScheduleData.filter((item) => item.date);




$mainTarget.innerHTML = '';


for(let i = 0; i < weekScheduleData.length; i++) {
    const weekScheduleItem = weekScheduleData[i]
    const weekScheduleCourses =  weekScheduleItem.courses;


    const $li = document.createElement('li');

    const $eventsList = document.createElement('ul');
    $eventsList.classList.add('week-schedule-list-courses')


    $li.classList.add('week-schedule-list__item')
    $li.style.display = 'none';

    $weekScheduleDate.innerHTML = weekScheduleItem.date;


    if(weekScheduleCourses) {

        for(let j = 0; j < weekScheduleCourses.length; j++) {
            const weekScheduleCourse = weekScheduleCourses[j];
            const $eventsListItem = document.createElement('li');

            let counter = j + 1

            $eventsListItem.innerHTML = '<span class="order-number">'+counter+'</span>'+'<a href="'+weekScheduleCourse.url+'">'+weekScheduleCourse.title+'</a>';

            $eventsList.append($eventsListItem);
        }

        $li.append($eventsList)

    }
    if(!weekScheduleCourses.length) {
        const noEventsBlock = document.createElement('li')
        noEventsBlock.classList.add('no-events')
        noEventsBlock.textContent = 'Немає уроків в цей день'
        $eventsList.append(noEventsBlock)
    }
    $mainTarget.appendChild($li);
}


updateVisibility(activeItem);




document.querySelector('.week-schedule.prev-btn').addEventListener('click', function() {
    if(activeItem < 1) return false;
    activeItem -= 1;
    [...document.querySelectorAll('.week-schedule-list__item')].forEach((item) => item.style.display = 'none');
    updateVisibility(activeItem)
})

document.querySelector('.week-schedule.next-btn').addEventListener('click', function() {
    if(activeItem + 1 > weekScheduleData.length - 1) return false;
    activeItem += 1;
    [...document.querySelectorAll('.week-schedule-list__item')].forEach((item) => item.style.display = 'none');
    updateVisibility(activeItem)
})




function updateVisibility(activeItem) {
    [...document.querySelectorAll('.week-schedule-list__item')][activeItem].style.display = 'block';
    $weekScheduleDate.textContent = weekScheduleData[activeItem].date
}

