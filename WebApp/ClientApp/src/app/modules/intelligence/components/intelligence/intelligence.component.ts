import { Component, OnInit, ViewChild } from '@angular/core';
import { FormGroup } from '@angular/forms';
import { Galleria } from 'primeng/galleria';
import { interval, Subscription } from 'rxjs';
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

  // status variables
  uploading = null;
  uploaded = false;
  uplodingValue;
  predicting = null;
  //splitting
  spliting = null; // 0-spliting 1-done
  fetchingPredicted = null;
  //variables
  processedImagesList: IImage[];
  searchValue: string;
  subscription: Subscription;
  constructor(
    private intelligenceService: IntelligenceService,
    private sweetAlert: SweetAlertService
  ) {}

  ngOnInit() {
    //this.getProcessedImagesList();
    // setInterval(function () {
    //   console.log('fetching data...!');
    //   this.getProcessedImagesList();
    // }, 5000); //run this thang every 2 seconds

    const source = interval(20000);
    this.subscription = source.subscribe((val) => {
      this.getProcessedImagesList();
      console.log('fetching data...!');
    });
  }
  ngOnDestroy() {
    this.subscription.unsubscribe();
  }
  uploadVideo(event): any {
    this.uploading = 0;
    this.uplodingValue = 50;
    const formData: any = new FormData();

    formData.append('file', event.files[0], event.files[0].name);
    

    this.intelligenceService.uploadVideo(formData).subscribe(
      (response) => {
        console.log(response);
        this.sweetAlert.success2('Uploaded video');
        this.uploading = 1;
        //this.uploaded = true;
        this.uplodingValue = 100;

        this.splitImagesFromVideo();
      },
      (error) => {
        console.log(error);
        this.sweetAlert.error3('Failed uploading video');
        // this.uploading = null;
        this.uploading = 2;
      }
    );
  }
  refresh() {
    //window.location.reload();
    this.getProcessedImagesList();
  }
  splitImagesFromVideo(): any {
    // this.predicting = true;
    //  this.processedImagesList = null;
    this.spliting = 0;
    this.intelligenceService.splitImagesFromVideo().subscribe(
      (response) => {
        console.log(response);
        //this.processedImagesList = response;
        this.spliting = 1;
        //this.predicting = false;
        this.sweetAlert.success('data successfully refreshed');
        this.startPredictionProcess();
      },
      (error) => {
        console.log(error);
        //this.predicting = false;
        this.sweetAlert.error3('failed spliting images');
        this.spliting = 2;
      }
    );
  }
  startPredictionProcess(): any {
    this.predicting = 0;
    // this.processedImagesList = null;
    this.intelligenceService.startPredictionProcess().subscribe(
      (response) => {
        this.predicting = 1;
        // console.log('my resoinse');
        console.log(response);
        // this.processedImagesList = response;

        // this.predicting = false;
        this.sweetAlert.success('finished prediction');

        this.getProcessedImagesList();
      },
      (error) => {
        this.predicting = 2;
        console.log(error);
        this.predicting = false;
        this.sweetAlert.error3('prediction failed');
      }
    );
  }
  getProcessedImagesList(): any {
    this.fetchingPredicted = 0;
    // this.predicting = true;
    this.processedImagesList = null;
    this.intelligenceService.getProcessedImages().subscribe(
      (response) => {
        this.fetchingPredicted = 1;
        console.log(response);
        this.processedImagesList = response;

        //this.predicting = false;
        this.sweetAlert.success('data successfully refreshed');
      },
      (error) => {
        this.fetchingPredicted = 2;
        console.log(error);
        //this.predicting = false;
        this.sweetAlert.error('Oops seems like nothing has been predicted yet, upload video');
      }
    );
  }
}
