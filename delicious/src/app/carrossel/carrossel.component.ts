import { Component, ElementRef, OnInit, ViewChild, AfterViewInit } from '@angular/core';

@Component({
  selector: 'app-carrossel',
  templateUrl: './carrossel.component.html',
  styleUrls: ['./carrossel.component.css'],
})
export class CarrosselComponent implements OnInit, AfterViewInit {
  @ViewChild('slidesContainer') slidesContainer!: ElementRef;

  currentIndex = 0;
  slideWidth: number;
  slides = [
    {image: '../../assets/bg1.jpg', text: 'SLIDE 1'},
    {image: '../../assets/bg6.jpg', text: 'SLIDE 2'},
    {image: '../../assets/bg7.jpg', text: 'SLIDE 3'},
    // Adicione mais slides conforme necessário
  ];


  constructor() {
    this.slideWidth = 0;
  }

  ngOnInit(): void {
    // Não é necessário calcular a largura do slide aqui
  }

  ngAfterViewInit(): void {
    this.calculateSlideWidth();
    this.updateSlidePosition();
  }

  updateSlidePosition(): void {
    if (this.slidesContainer) {
      this.slidesContainer.nativeElement.style.transform = `translateX(${-this.currentIndex * this.slideWidth}px)`;
    }
  }

  calculateSlideWidth(): void {
    if (this.slidesContainer) {
      this.slideWidth = this.slidesContainer.nativeElement.clientWidth;
    }
  }

  goToPrevSlide(): void {
    this.currentIndex = Math.max(this.currentIndex - 1, 0);
    this.updateSlidePosition();
  }

  goToNextSlide(): void {
    this.currentIndex = Math.min(this.currentIndex + 1, this.slides.length - 1);
    this.updateSlidePosition();
  }
  
}