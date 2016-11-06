package com.example.android.camera2basic;

import android.app.Activity;
import android.os.Bundle;
import android.widget.ImageView;

import com.squareup.picasso.Picasso;

/**
 * Created by Md Islam on 8/13/2016.
 */
public class ImageViewActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_imageview);
        setTitle("Gallery");

        ImageView imageView = (ImageView) findViewById(R.id.image);
        Picasso.with(this).load("http://104.236.246.190/uploads/sadface.jpg").into(imageView);
    }



}
