import { CommonModule } from '@angular/common';
import { ChangeDetectionStrategy, Component, Input } from '@angular/core';
import { RouterModule, RouterOutlet } from '@angular/router';
import { NzModule } from '../../modules/nz.module';
import { SidebarOption } from './sidebar-model';
import { TranslateModule } from '@ngx-translate/core';
import { UserInfoComponent } from '../user-info/user-info.component';
import { IconPath } from '../../models/paths-to-resources';
import { KeycloakService } from '../../auth/keycloak.service';
import { TokenParsed } from '../../types/authTypes';

@Component({
  selector: 'app-sidebar',
  standalone: true,
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush,
  imports: [CommonModule, NzModule, RouterOutlet, RouterModule, TranslateModule, UserInfoComponent],
})
export class SidebarComponent {
  tokenParsed: TokenParsed = KeycloakService.getTokenParsed()
  @Input() sidebarOptions?: SidebarOption[] | null
  @Input() isSidebarCollapsed = false
  readonly IconPath = IconPath

  logout(): void {
    KeycloakService.logout()
  }
}
