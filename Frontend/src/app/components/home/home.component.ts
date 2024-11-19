import { ChangeDetectionStrategy, Component } from '@angular/core';
import { ALL_MENU_OPTIONS } from '../../shared/components/sidebar/sidebar-options';
import { IconPath } from '../../shared/models/paths-to-resources';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class HomeComponent {
  readonly IconPath = IconPath
  sidebarOptions = ALL_MENU_OPTIONS
  isSidebarCollapsed = false
}
