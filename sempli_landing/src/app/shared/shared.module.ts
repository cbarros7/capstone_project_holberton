import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { AboutComponent } from './about/about.component';
import { ContactComponent } from './contact/contact.component';
import { FooterComponent } from './footer/footer.component';
import { ProcessComponent } from './process/process.component';
import { BenefitsComponent } from './benefits/benefits.component';
import { TeamComponent } from './team/team.component';

import { FeatherModule } from 'angular-feather';
import {
  Mail, Link, PhoneCall, Clock, MapPin, Facebook, Twitter, Instagram, Linkedin, Send, Calendar, User, Server, Rss, Layout, LifeBuoy,
  ArrowRightCircle, PieChart, Triangle
} from 'angular-feather/icons';
import { ScrollspyDirective } from './scrollspy.directive';



const icons = {
  Mail, Link, PhoneCall, Clock, MapPin, Facebook, Twitter, Instagram, Linkedin, Send, Calendar, User, Server, Rss, Layout, LifeBuoy,
  ArrowRightCircle, PieChart, Triangle
};

@NgModule({
  // tslint:disable-next-line: max-line-length
  declarations: [AboutComponent, ContactComponent, FooterComponent, ScrollspyDirective, ProcessComponent, BenefitsComponent, TeamComponent],
  imports: [
    CommonModule,
    FeatherModule.pick(icons)
  ],
  // tslint:disable-next-line: max-line-length
  exports: [AboutComponent, ContactComponent, FooterComponent, ProcessComponent, BenefitsComponent, TeamComponent, FeatherModule, ScrollspyDirective]
})
export class SharedModule { }
