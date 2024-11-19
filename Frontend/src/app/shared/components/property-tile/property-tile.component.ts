import { CommonModule } from '@angular/common'
import { ChangeDetectionStrategy, Component, Input, OnInit } from '@angular/core'
import { FormsModule } from '@angular/forms'
import { NzModule } from '../../modules/nz.module'
import { DomSanitizer, SafeUrl } from '@angular/platform-browser'
import { IconPath } from '../../models/paths-to-resources'
import { PropertyType } from '../../models/property.model'
import { RouterLink } from "@angular/router"
import { PricePipe } from "../../pipes/price.pipe"


@Component({
  selector: 'app-property-tile',
  standalone: true,
  templateUrl: './property-tile.component.html',
  styleUrls: ['./property-tile.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush,
  imports: [CommonModule, FormsModule, NzModule, RouterLink, PricePipe]
})
export class PropertyTileComponent implements OnInit {
  @Input() property!: PropertyType
  @Input() last: boolean = false;
  sanitizedImageData!: SafeUrl;
  readonly IconPath = IconPath

  constructor(private readonly sanitizer: DomSanitizer) { }

  ngOnInit() {
    this.sanitizedImageData = this.sanitizer.bypassSecurityTrustUrl(this.property.image.imageData.replace(/,\\n$/, ''))
  }

}
