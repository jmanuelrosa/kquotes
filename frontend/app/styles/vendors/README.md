
## material-icons (material-design-iconic-font)

    - Download material-design-iconic-font
      ```
      bower install material-design-iconic-font
      ```

    - Copy fonts and sass files
      ```
      cp -r bower_components/material-design-iconic-font/fonts/* app/fonts/
      cp -r bower_components/material-design-iconic-font/scss/* app/styles/vendors/material-icons/
      ```

    - Edit ```app/styles/vendors/material-icons/_variables.scss``` to chenge the font path and the prefix
      ```
      (...)
      $md-font-path: "../../../fonts";
      $md-css-prefix: md-icon;
      (...)
      ```
