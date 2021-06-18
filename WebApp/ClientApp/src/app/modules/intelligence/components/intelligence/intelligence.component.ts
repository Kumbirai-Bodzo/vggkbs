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

  uploading = false;
  uploaded = false;
  uplodingValue;
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
  uploadVideo(event): any {
    this.uploading = true;
    this.uplodingValue = 50;
    const formData: any = new FormData();

    formData.append('video', event.files[0], event.files[0].name);
    //formData.append('accommodation', this.accommodationId);
    console.log(event);
    // this.upLoadSingles(formData);

    this.intelligenceService.uploadVideo(formData).subscribe(
      (response) => {
        console.log(response);
        this.sweetAlert.success2('Uploaded video');
        this.uploading = false;
        this.uploaded = true;
        this.uplodingValue = 100;
      },
      (error) => {
        console.log(error);
        this.sweetAlert.error3('Failed uploading some images');
        this.uploading = false;
         this.uplodingValue = 0;
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
}
