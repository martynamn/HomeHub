import { CommonModule } from '@angular/common';
import { ChangeDetectionStrategy, Component, Input } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { NzModule } from '../../modules/nz.module';
import { fadeInAnimation } from '../../animations/fade-in';
import { SidebarComponent } from '../sidebar/sidebar.component';
import { IconPath } from '../../models/paths-to-resources';
import { PieChartIcons, PieChartTitle, TileType } from './pie-chart-tile.model';

@Component({
  selector: 'app-pie-chart-tile',
  standalone: true,
  animations: [fadeInAnimation],
  templateUrl: './pie-chart-tile.component.html',
  styleUrls: ['./pie-chart-tile.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush,
  imports: [CommonModule, NzModule, RouterOutlet, SidebarComponent]
})
export class PieChartTileComponent {
  readonly IconPath = IconPath
  readonly PieChartIcons: any = PieChartIcons
  readonly PieChartTitle: any = PieChartTitle
  @Input() tiles!: TileType[]
}
