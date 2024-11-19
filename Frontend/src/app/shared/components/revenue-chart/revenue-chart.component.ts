import { ChangeDetectionStrategy, Component, Input } from '@angular/core'
import { CommonModule } from "@angular/common"
import { NzModule } from "../../modules/nz.module"
import { EChartsOption } from "echarts"
import { NgxEchartsModule } from "ngx-echarts"
import { RevenueChart, RevenueChartType, revenueModel } from "./revenue-chart.model"
import { TranslateService } from "@ngx-translate/core"

@Component({
  selector: 'app-revenue-chart',
  standalone: true,
  templateUrl: './revenue-chart.component.html',
  styleUrls: ['./revenue-chart.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush,
  imports: [CommonModule, NzModule, NgxEchartsModule]
})

export class RevenueChartComponent {
  @Input() chartData!: RevenueChartType
  chartOption: EChartsOption = {}

  constructor(private readonly translate: TranslateService) { }
  ngOnInit() {
    this.chartOption = this.createChartConfiguration(this.chartData)
  }

  private convertRevenue(revenue: number): string {
    return revenue.toString().replace(revenueModel, ",")
  }

  private createChartConfiguration(chartData: RevenueChartType): EChartsOption {
    return {
      title: {
        text: this.translate.instant("Total Revenue"),
        subtext: `$${this.convertRevenue(chartData.totalRevenue)}`,
        itemGap: 20,
        padding: [40, 20, 60, 28],
        textStyle: {
          fontSize: 20,
          fontWeight: "normal",
          color: "#000000"
        },
        subtextStyle: {
          fontSize: 26,
          fontWeight: "bold",
          color: "#000000",
        }
      },
      legend: {
        orient: 'horizontal',
        left: 'right',
        padding: [40, 28, 60, 80],
      },
      tooltip: {
        trigger: 'axis',
        axisPointer: {
          type: 'shadow'
        }
        ,
      },
      xAxis: {
        type: 'category',
        data: chartData.currentYear.map((item: RevenueChart) => item.month),
        axisTick: {
          show: false
        },
        axisLine: {
          show: false
        },
      },
      yAxis: {
        type: 'value',
        axisLabel: {
          formatter: (value: any): string => {
            return this.convertRevenue(value)
          }
        },
        splitLine: {
          show: false
        }
      },
      color: ["#475be8", "#CFC8FF"],
      barWidth: "30%",
      barGap: "8%",
      barBorderRadius: 5,
      itemStyle: {
        borderRadius: 4
      },
      grid: {
        show: false,
        top: 140
      },
      series: [{
        data: chartData.lastYear.map((item: RevenueChart) => item.revenue),
        type: 'bar',
        name: chartData.lastYear[0].year,
      },
      {
        data: chartData.currentYear.map((item: RevenueChart) => item.revenue),
        type: 'bar',
        name: chartData.currentYear[0].year,
      }],
    }
  }
}

