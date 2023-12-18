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
    {image: '../../assets/bg1.jpg', text: 'FUNCIONA??'},
    {image: '../../assets/bg6.jpg', text: 'Nop'},
    {image: '../../assets/bg7.jpg', text: 'Sim'},
    // Adicione mais slides conforme necessário
  ];

  constructor() {
    this.slideWidth = 0;
  }

  ngOnInit(): void {
    // Não é necessário calcular a largura do slide aqui
  }

  ngAfterViewInit(): void {
    // Chame a função para calcular a largura do slide após a exibição da visualização
    this.calculateSlideWidth();
    // Atualize a posição do slide após a exibição da visualização
    this.updateSlidePosition();
  }

  updateSlidePosition(): void {
    if (this.slidesContainer) {
      this.slidesContainer.nativeElement.style.transform = `translateX(${-this.currentIndex * this.slideWidth}px)`;
    }
  }

  calculateSlideWidth(): void {
    if (this.slidesContainer) {
      // Defina a largura do slide para ser igual à largura do carrossel
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