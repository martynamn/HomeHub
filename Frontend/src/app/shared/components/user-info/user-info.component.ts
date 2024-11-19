import { CommonModule } from '@angular/common'
import { ChangeDetectionStrategy, Component, Input } from '@angular/core'
import { RouterModule } from '@angular/router'

import { TranslateModule } from '@ngx-translate/core'
import { NzModule } from '../../modules/nz.module'
import { TokenParsed } from '../../types/authTypes'

@Component({
  standalone: true,
  selector: 'app-user-info',
  imports: [CommonModule, NzModule, RouterModule, TranslateModule],
  templateUrl: './user-info.component.html',
  styleUrls: ['./user-info.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class UserInfoComponent {
  @Input() tokenParsed!: TokenParsed
}
