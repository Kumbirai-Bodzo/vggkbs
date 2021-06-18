import { Component, OnInit, ViewChild } from '@angular/core';
import { FormGroup } from '@angular/forms';
import { Galleria } from 'primeng/galleria';
import { SweetAlertService } from 'src/app/application-shared/services/sweetAlert/sweetAlert.service';
import { IImage } from '../../interfaces/IImage';
import { IntelligenceService } from '../../services/intelligence.service';
//import { Galleria } from 'primeng/galleria';
@Component({
  selector: 'app-intelligence',
  templateUrl: './intelligence.component.html',
  styleUrls: ['./intelligence.component.scss'],
})
export class IntelligenceComponent implements OnInit {
  uploadedFiles: any[] = [];
  @ViewChild('galleria') galleria: Galleria;
  galleryForm: FormGroup;
  uploadProgressCounter = 0; // percentage
  uploadedCounter = 0;
  totalFilesToUpload = 0;
  uploadTriggered = false;
  uploadLimits: any;
  //variables
  processedImagesList: IImage[];
  searchValue: string;
  constructor(
    private intelligenceService: IntelligenceService,
    private sweetAlert: SweetAlertService
  ) {}

  ngOnInit() {
    this.getProcessedImagesList();

  }
uploadVideo(event):any{
  const formData: any = new FormData();

  formData.append('video', event.files[0], event.files[0].name);
  //formData.append('accommodation', this.accommodationId);
console.log(event)
 // this.upLoadSingles(formData);

  this.intelligenceService.uploadVideo(formData).subscribe(
    (response) => {
      console.log(response);
    },
    (error) => {
      console.log(error);
      this.sweetAlert.error3('Failed uploading some images');
    }
  );
}
  getProcessedImagesList(): any {
    this.processedImagesList = null;
    this.intelligenceService.getProcessedImages().subscribe(
      (response) => {
        console.log('my resoinse');
        console.log(response);
        this.processedImagesList = response;
        // this.uploadLimits = response;
        // this.imageList = response;
      },
      (error) => {
        console.log(error);
        // this.sweetAlert.error3('Failed uploading some images');
      }
    );
  }

  submitAccommodationGallery(event): any {
    // let uploadedCounter = 0;
    this.totalFilesToUpload = event.files.length;

    this.uploadTriggered = true;

    for (const file of event.files) {
      const formData: any = new FormData();

      console.log(file);
      formData.append('image', event.files, event.files.name);
      //formData.append('accommodation', this.accommodationId);

      this.upLoadSingles(formData);
    }

    // this.uploadedCounter = 0;
    /*  this.formData.append('image', this.galleryForm.get('image').value);*/
    // console.log(formData.entries());
    // console.log(formData.getAll('accommodation'));
  }

  upLoadSingles(formData): any {
    // this.accommodationService.accommodationAddGallery(formData).subscribe(
    //   (response) => {
    //     console.log(response);
    //   },
    //   (error) => {
    //     console.log(error);
    //     this.sweetAlert.error3('Failed uploading some images');
    //   }
    // );
  }
}
