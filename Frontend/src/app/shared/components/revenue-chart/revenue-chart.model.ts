export interface RevenueChartType {
  currentYear: RevenueChart[]
  lastYear: RevenueChart[]
  totalRevenue: number
}

export interface RevenueChart {
  revenue: number
  month: string
  year: number
}

export const revenueModel = /\B(?=(\d{3})+(?!\d))/g
