var metronome = new Metronome();
var tempo = document.getElementById('tempo');
var tempoDisplayElem = document.getElementById('tempo-display');


function updateDisplay(){
    tempoDisplayElem.innerHTML = metronome.tempo + ' ' + 'BPM';
};

updateDisplay();

var playButton = document.getElementById('play-button');
playButton.addEventListener('click', function() {
    metronome.start();
});

var pauseButton = document.getElementById('pause-button');
pauseButton.addEventListener('click', function() {
    metronome.stop();
});

var tempoChangeButtons = document.getElementsByClassName('tempo-change');
for (var i = 0; i < tempoChangeButtons.length; i++) {
    tempoChangeButtons[i].addEventListener('click', function() {
        metronome.tempo += parseInt(this.dataset.change);
        tempoDisplayElem.innerHTML = metronome.tempo + ' ' + 'BPM';
    });
}

