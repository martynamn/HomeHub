import { ChangeDetectionStrategy, Component } from '@angular/core'
import { DashboardService } from '../../../../shared/services/dashboard.service'
import { TileType } from 'src/app/shared/components/pie-chart-tile/pie-chart-tile.model'
import { Observable } from 'rxjs'
import { PropertyService } from "../../../../shared/services/property.service"
import { PropertyType } from "../../../../shared/models/property.model"
import { RevenueChartType } from "../../../../shared/components/revenue-chart/revenue-chart.model"
import { KeycloakService } from "../../../../shared/auth/keycloak.service"
import { UserParam } from "../../../../shared/models/profile.model"
import { IconPath } from "../../../../shared/models/paths-to-resources"

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class DashboardComponent {
  numberOfProperties: number = 3
  year: number = new Date().getFullYear()
  userParam: UserParam = { key: 'userId', value: this.keycloakService.getUserId() }
  dashboardTiles$: Observable<TileType[]> = this.dashboardService.getDashboardTiles(this.userParam)
  lastProperties$: Observable<PropertyType[]> = this.propertyService.getLastProperties(this.userParam, this.numberOfProperties)
  chartData$: Observable<RevenueChartType> = this.dashboardService.getRevenue(this.userParam, this.year)
  

  constructor(
    private readonly dashboardService: DashboardService,
    private readonly propertyService: PropertyService,
    private readonly keycloakService: KeycloakService
  ) { }

  protected readonly IconPath = IconPath;
}
