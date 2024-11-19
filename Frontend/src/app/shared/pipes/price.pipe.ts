import {Pipe, PipeTransform} from '@angular/core';
import { revenueModel } from '../components/revenue-chart/revenue-chart.model';

@Pipe({
  name: 'pricePipe',
  standalone: true
})

export class PricePipe implements PipeTransform {
  transform(value: any): any {
    const result = value.toString().replace(revenueModel, ",")
    return result;
  }
}