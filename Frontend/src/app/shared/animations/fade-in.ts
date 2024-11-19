import { style, transition, trigger, animate } from '@angular/animations'

export const fadeInAnimation = trigger('fadeInAnimation', [
  transition(':enter', [style({ opacity: 0 }), animate('1.5s ease-out', style({ opacity: 1 }))]),
])
