var metronome = new Metronome();
var tempo = document.getElementById('tempo');
var tempoDisplayElem = document.getElementById('tempo-display');

updateDisplay();

function updateDisplay(){
    tempoDisplayElem.innerHTML = metronome.tempo + 'BPM';
};

var playButton = document.getElementById('play-button');
playButton.addEventListener('click', function() {
    metronome.start();
    updateDisplay();
});

var pauseButton = document.getElementById('pause-button');
pauseButton.addEventListener('click', function() {
    metronome.stop();
    updateDisplay();
});

var tempoChangeButtons = document.getElementsByClassName('tempo-change');
for (var i = 0; i < tempoChangeButtons.length; i++) {
    tempoChangeButtons[i].addEventListener('click', function() {
        metronome.tempo += parseInt(this.dataset.change);
        tempo.textContent = metronome.tempo;
    });
    updateDisplay();
}

