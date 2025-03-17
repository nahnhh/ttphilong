import time
import random
import keyboard
from pathlib import Path
from rich.console import Console
from playsound import playsound

soundfile = Path(__file__).parent / 'harp.mp3' # replace with your sound
soundfile = str(soundfile)
console = Console()

def stop_after(sleep_interval):
  time.sleep(sleep_interval)
  console.print("STOP! YOU GO.", style="bold red")

def inputs():
  global total_time, avg_time, r_min, r_max, presenters
  total_time = int(input("Total time (in minutes, default = 20): ") or 20)
  presenters = input("Name of presenters (A B ..): ")
  presenters = list(presenter for presenter in presenters.split(' '))

  rand_ko = input("Random order? [Y/n]: ")
  if rand_ko == '' or 'y' or 'Y':
    random.shuffle(presenters)
  avg_time = total_time / len(presenters) * 60
  r_min, r_max = -avg_time/4, avg_time/4

  print(f'Time for each presenter = {total_time / len(presenters):.2f} minutes + ({r_min:.2f}, {r_max:.2f})s')
  print()
  console.print(f"{presenters[0].upper()} WILL BE THE FIRST ONE TO PRESENT.", style="bold yellow")
  time.sleep(4)
  console.print("YOUR TIME STARTS...", style="bold yellow")
  time.sleep(2)
  console.print("NOW.", style="bold yellow")
  print()


def main():
  inputs()
  time_left = total_time * 60
  for i, p in enumerate(presenters):
    console.print(f'{p.upper()}, YOU PRESENT.', style="bold yellow")
    playsound(soundfile)
    sleep_interval = avg_time + random.uniform(r_min, r_max)
    
    if i < len(presenters) - 1:
      time_left = time_left - sleep_interval
      console.print(f"{p.upper()} will present for {sleep_interval/60:.2f} minutes ({time_left/60:.2f} minutes left)", style="bold blue")
      stop_after(sleep_interval)
    else: # last presenter
      sleep_interval = time_left + random.uniform(-(time_left/32), time_left/8)
      console.print(f"{p.upper()} is the last to present for {sleep_interval/60:.2f} minutes (end of time)", style="bold blue")
      stop_after(sleep_interval)

  playsound(soundfile)
  console.print("PRESENTATION IS OVER.", style="bold yellow")

if __name__ == "__main__":
  main()