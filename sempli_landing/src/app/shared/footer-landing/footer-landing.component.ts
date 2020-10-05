import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-footer-landing',
  templateUrl: './footer-landing.component.html',
  styleUrls: ['./footer-landing.component.scss']
})
export class FooterLandingComponent implements OnInit {

  year: number = new Date().getFullYear();
  constructor() { }

  ngOnInit(): void {
  }

}
