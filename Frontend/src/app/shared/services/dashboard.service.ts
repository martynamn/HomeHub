import { HttpClient, HttpParams } from '@angular/common/http'
import { Injectable } from '@angular/core'
import { Observable } from 'rxjs'
import { environment } from 'src/app/environments/environment'
import { TileType } from '../components/pie-chart-tile/pie-chart-tile.model'
import { RevenueChartType } from "../components/revenue-chart/revenue-chart.model"
import { UserParam } from "../models/profile.model"

@Injectable({ providedIn: 'root' })
export class DashboardService {
  private readonly API_URI = environment.apiUrl

  constructor(
    private readonly httpClient: HttpClient,
  ) { }

  getDashboardTiles(userParam: UserParam): Observable<TileType[]> {
    let params = new HttpParams().append(userParam.key, userParam.value)
    return this.httpClient.get<TileType[]>(`${this.API_URI}dashboard`, { params: params })
  }

  getRevenue(userParam: UserParam, year: number): Observable<RevenueChartType> {
    let params = new HttpParams().append(userParam.key, userParam.value)
    return this.httpClient.get<RevenueChartType>(`${this.API_URI}dashboard/revenue/${year}`, { params: params })
  }

}
