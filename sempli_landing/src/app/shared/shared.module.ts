// Modules
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FeatherModule } from 'angular-feather';

// Components
import { AboutComponent } from './about/about.component';
import { ContactComponent } from './contact/contact.component';
import { FooterLandingComponent } from './footer-landing/footer-landing.component';
import { ProcessComponent } from './process/process.component';
import { TeamComponent } from './team/team.component';
import { HeaderComponent } from './components/header/header.component';
import { SidebarComponent } from './components/sidebar/sidebar.component';
import { FooterDashComponent } from './components/footer-dash/footer-dash.component';

// Angular Feather Icons
import {
  Mail, Link, PhoneCall, Clock, MapPin, Facebook, Twitter, Instagram, Linkedin, Send, Calendar, User, Server, Rss, Layout, LifeBuoy,
  ArrowRightCircle, PieChart, Triangle, Github
} from 'angular-feather/icons';
import { ScrollspyDirective } from './scrollspy.directive';



const icons = {
  Mail, Link, PhoneCall, Clock, MapPin, Facebook, Twitter, Instagram, Linkedin, Send, Calendar, User, Server, Rss, Layout, LifeBuoy,
  ArrowRightCircle, PieChart, Triangle, Github
};

@NgModule({
  // tslint:disable-next-line: max-line-length
  declarations: [AboutComponent, ContactComponent, FooterLandingComponent, ScrollspyDirective, ProcessComponent, TeamComponent, HeaderComponent, SidebarComponent, FooterDashComponent],
  imports: [
    CommonModule,
    FeatherModule.pick(icons)

  ],
  // tslint:disable-next-line: max-line-length
  exports: [AboutComponent, ContactComponent, FooterLandingComponent, ProcessComponent, TeamComponent, HeaderComponent, SidebarComponent, FooterDashComponent, FeatherModule, ScrollspyDirective, CommonModule]
})
export class SharedModule { }
