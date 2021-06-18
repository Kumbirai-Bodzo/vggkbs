export class CCarouselMobileSlider {
  primengCarouselSwipeFix = false;
  // failures

  constructor() {}
  public carouselSliderContainer(): boolean {
    const carousels = document.querySelectorAll('.p-carousel-items-container');

    if (carousels.length > 0) {
      console.log('carousels', carousels);
      carousels.forEach((carousel: any) => {
        console.log(
          'fix carousel vertical swipe on touch event based device',
          carousel
        );
        const fixEventIndex = 3;
        carousel.removeEventListener(
          'touchmove',
          carousel.eventListeners()[fixEventIndex]
        );
      });
      return true;

      this.primengCarouselSwipeFix = true;
    }
  }
}
