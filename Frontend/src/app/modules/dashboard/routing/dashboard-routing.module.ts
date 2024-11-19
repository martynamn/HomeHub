// Angular modules
import { NgModule } from '@angular/core'
import { CommonModule } from '@angular/common'
import { Routes, RouterModule } from '@angular/router'
// App components
import { DashboardComponent } from '../components/dashboard/dashboard.component'

const routes: Routes = [{path: '', component: DashboardComponent}]
@NgModule({
  declarations: [],
  imports: [CommonModule, RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class DashboardRoutingModule {}
