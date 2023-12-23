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
    {image: '../../assets/bg1.jpg', text: 'Explore a variety of delicious recipes available. From main dishes to incredible desserts, discover new flavors, get inspired and start cooking your own gastronomic creations.'},
    {image: '../../assets/bg6.jpg', text: 'Be a chef in your own kitchen! Add your special creations, describe the ingredients and preparation steps, and inspire others to try your delicious recipes.'},
    {image: '../../assets/bg7.jpg', text: 'Open the virtual doors of your personal refrigerator. You can add, remove, and update items as needed, ensuring you are always ready to create your favorite recipes.'},
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