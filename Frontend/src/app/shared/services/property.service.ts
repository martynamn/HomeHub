import { HttpClient, HttpParams } from '@angular/common/http'
import { Injectable } from '@angular/core'
import { Observable } from 'rxjs'
import { environment } from 'src/app/environments/environment'
import { filterData } from '../components/filter/filter.model'
import { PropertyType } from '../models/property.model'
import { UserParam } from "../models/profile.model"

@Injectable({ providedIn: 'root' })
export class PropertyService {
  private readonly API_URI = environment.apiUrl

  constructor(private readonly httpClient: HttpClient) { }

  getPropertyInfo(propertyId: string): Observable<PropertyType> {
    return this.httpClient.get<PropertyType>(`${this.API_URI}property/${propertyId}`)
  }

  getProperties(pageIndex: number, pageSize: number, filterParams?: filterData[]): Observable<PropertyType[]> {
    let params = new HttpParams().append('index', pageIndex).append('limit', pageSize)
    if (filterParams?.length) {
      filterParams.forEach(param => {
        params = params.append(param.key, param.value);
      });
    }
    return this.httpClient.get<PropertyType[]>(`${this.API_URI}property/`, { params: params })
  }

  saveProperty(formData: FormData) {
    return this.httpClient.post<PropertyType[]>(`${this.API_URI}property`, formData)
  }

  getLastProperties(userParam: UserParam, numberOfProperties: number): Observable<PropertyType[]> {
    let params = new HttpParams().append(userParam.key, userParam.value)
    return this.httpClient.get<PropertyType[]>(`${this.API_URI}property/latest/${numberOfProperties}`, { params: params })
  }

  updateProperty(id: string, formData: FormData) {
    return this.httpClient.put<any>(`${this.API_URI}property/${id}`, formData)
  }


  soldProperty(property: PropertyType) {
    return this.httpClient.put(`${this.API_URI}property/${property._id}/sold`, property)
  }

  deleteProperty(property: PropertyType) {
    return this.httpClient.delete(`${this.API_URI}property/${property._id}`)
  }


}
