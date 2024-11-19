import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { TranslateModule } from '@ngx-translate/core';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { DashboardRoutingModule } from './routing/dashboard-routing.module';
import { PieChartTileComponent } from 'src/app/shared/components/pie-chart-tile/pie-chart-tile.component';
import { PropertyTileComponent } from '../../shared/components/property-tile/property-tile.component';
import { NgxEchartsModule } from 'ngx-echarts';
import { RevenueChartComponent } from '../../shared/components/revenue-chart/revenue-chart.component';
import { NzModule } from '../../shared/modules/nz.module';
import { LatestPropertiesComponent } from '../../shared/components/latest-properties/latest-properties.component';

@NgModule({
  declarations: [DashboardComponent],
  imports: [
    CommonModule,
    DashboardRoutingModule,
    TranslateModule,
    PieChartTileComponent,
    RevenueChartComponent,
    PropertyTileComponent,
    LatestPropertiesComponent,
    NgxEchartsModule.forRoot({
      echarts: () => import('echarts'),
    }),
    NzModule,
  ],
  exports: [DashboardComponent],
  providers: [],
})
export class DashboardModule {}
