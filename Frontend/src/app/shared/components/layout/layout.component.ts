import { CommonModule } from '@angular/common';
import { ChangeDetectionStrategy, Component, Input } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { NzModule } from '../../modules/nz.module';
import { SidebarOption } from '../sidebar/sidebar-model';
import { fadeInAnimation } from '../../animations/fade-in';
import { SidebarComponent } from '../sidebar/sidebar.component';

@Component({
  selector: 'app-layout',
  standalone: true,
  animations: [fadeInAnimation],
  templateUrl: './layout.component.html',
  styleUrls: ['./layout.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush,
  imports: [CommonModule, NzModule, RouterOutlet, SidebarComponent]
})
export class LayoutComponent {
  @Input() appName!: string
  @Input() sidebarOptions?: SidebarOption[] | null
  @Input() sidebarWidth = 280
  @Input() logoPath!: string
  isSidebarCollapsed = false
}
