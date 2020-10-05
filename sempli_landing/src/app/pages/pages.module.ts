import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { IndexComponent } from './index/index.component';
import { DashboardComponent } from './dashboard/dashboard.component';

import { ScrollToModule } from '@nicky-lenaers/ngx-scroll-to';

import { PagesRoutingModule } from './pages-routing.module';

import { SharedModule } from '../shared/shared.module';



@NgModule({
  declarations: [
    IndexComponent,
    DashboardComponent

],
  imports: [
    CommonModule,
    PagesRoutingModule,
    SharedModule,
    ScrollToModule.forRoot()
  ]
})
export class PagesModule { }
