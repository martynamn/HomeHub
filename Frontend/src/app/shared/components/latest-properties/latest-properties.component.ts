import { ChangeDetectionStrategy, Component, Input } from '@angular/core'
import { PropertyType } from "../../models/property.model"
import { IconPath } from "../../models/paths-to-resources"
import { CommonModule } from "@angular/common"
import { NzModule } from "../../modules/nz.module"
import { TranslateModule } from "@ngx-translate/core"
import { PropertyTileComponent } from "../property-tile/property-tile.component"
import { RouterLink } from "@angular/router"

@Component({
  selector: 'app-latest-properties',
  standalone: true,
  templateUrl: './latest-properties.component.html',
  styleUrls: ['./latest-properties.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush,
  imports: [CommonModule, NzModule, TranslateModule, PropertyTileComponent, RouterLink]
})

export class LatestPropertiesComponent {
  @Input() lastProperties: PropertyType[] | undefined
  protected readonly IconPath = IconPath
}
