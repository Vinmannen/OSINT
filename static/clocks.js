//source https://stackoverflow.com/questions/44081155/adding-multiple-clocks-in-multiple-time-zones

const clocks = document.getElementsByClassName("clock");

function updateClocks() {
  for (let clock of clocks) {
    let timezone = clock.dataset.timezone;
    let time = new Date().toLocaleTimeString("no-NO", {
      hour: '2-digit',
      minute:'2-digit',
      second: '2-digit',
      timeZone: timezone
    });
    clock.textContent = time;
  }
}

// Update every minute:
setInterval(updateClocks, 60);
updateClocks();