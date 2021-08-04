$(document).ready(function(){
    var newPhase = document.getElementById('phase');
    function addPhase(){
        var title = document.createElement('input');
        title.setAttribute('name', 'phase_title');
        title.setAttribute('id', 'phase_title');
        title.setAttribute('type', 'text');

        var date = document.createElement('input');
        date.setAttribute('name', 'phase_date');
        date.setAttribute('id', 'phase_date');
        date.setAttribute('type', 'date');

        document.getElementById('form')[0].appendChild(title);

        document.getElementById('form')[0].appendChild(date);
    }

    var newTask = document.getElementById('task');
    function addTask(){
        var title = document.createElement('input');
        title.setAttribute('name', 'task_title');
        title.setAttribute('id', 'task_title');
        title.setAttribute('type', 'text');

        var date = document.createElement('input');
        date.setAttribute('name', 'task_date');
        date.setAttribute('id', 'task_date');
        date.setAttribute('type', 'date');

        document.getElementById('form')[0].appendChild(title);

        document.getElementById('form')[0].appendChild(date);
    }
});