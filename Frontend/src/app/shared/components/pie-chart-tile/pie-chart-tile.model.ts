import { IconPath } from "../../models/paths-to-resources";

export interface TileType {
  name: string
  value: number
}

export enum PieChartIcons {
  sale = IconPath.BLUE_CHART,
  rent = IconPath.ORANGE_CHART,
  country = IconPath.GREEN_CHART,
  city = IconPath.PINK_CHART
}

export enum PieChartTitle {
  sale = 'Properties for Sale',
  rent = 'Properties for Rent',
  country = 'Total Countries',
  city = 'Total Cities',
}
