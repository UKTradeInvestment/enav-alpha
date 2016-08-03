// GULPFILE
// - - - - - - - - - - - - - - -
// This file processes all of the assets in the "apps/assets" folder
// and outputs the finished files in the "staticfiles" folder.

// LIBRARIES
// - - - - - - - - - - - - - - -
import gulp from 'gulp';
import stylish from 'jshint-stylish';
import paths from './projectpath.babel';
import loadPlugins from 'gulp-load-plugins';
import karma from 'karma';

const plugins = loadPlugins();


// TASKS
// - - - - - - - - - - - - - - -

// Move template resources

gulp.task('copy:govuk_template:template', () => gulp.src(paths.template + 'views/layouts/govuk_template.html')
  .pipe(gulp.dest(paths.templates))
);

gulp.task('copy:govuk_template:css', () => gulp.src(paths.template + 'assets/stylesheets/**/*.css')
  .pipe(plugins.sass({
    outputStyle: 'compressed'
  }))
  .on('error', plugins.sass.logError)
  .pipe(plugins.cssUrlAdjuster({
    prependRelative: '/static/',
  }))
  .pipe(gulp.dest(paths.dist + 'stylesheets/'))
);

gulp.task('copy:govuk_template:js', () => gulp.src(paths.template + 'assets/javascripts/**/*.js')
  .pipe(plugins.uglify())
  .pipe(gulp.dest(paths.dist + 'javascripts/'))
);

gulp.task('copy:govuk_template:images', () => gulp.src(paths.template + 'assets/stylesheets/images/**/*')
  .pipe(gulp.dest(paths.dist + 'images/'))
);

gulp.task('javascripts', () => gulp
  .src([
    paths.toolkit + 'javascripts/govuk/modules.js',
    paths.toolkit + 'javascripts/govuk/selection-buttons.js',
    paths.src + 'javascripts/detailsPolyfill.js',
    paths.src + 'javascripts/apiKey.js',
    paths.src + 'javascripts/autofocus.js',
    paths.src + 'javascripts/highlightTags.js',
    paths.src + 'javascripts/fileUpload.js',
    paths.src + 'javascripts/updateContent.js',
    paths.src + 'javascripts/expandCollapse.js',
    paths.src + 'javascripts/**/*.js',

  ])
  .pipe(plugins.babel({
    presets: ['es2015']
  }))
  .pipe(plugins.uglify())
  .pipe(plugins.addSrc.prepend([
    paths.npm + 'jquery/dist/jquery.min.js',
    paths.npm + 'query-command-supported/dist/queryCommandSupported.min.js',
    paths.npm + 'diff-dom/diffDOM.js'
  ]))
  .pipe(plugins.concat('all.js'))
  .pipe(gulp.dest(paths.dist + 'javascripts/'))
);

// don't uglify the JS
gulp.task('debugjs', () => gulp
  .src([
    paths.toolkit + 'javascripts/govuk/modules.js',
    paths.toolkit + 'javascripts/govuk/selection-buttons.js',
    paths.src + 'javascripts/detailsPolyfill.js',
    paths.src + 'javascripts/apiKey.js',
    paths.src + 'javascripts/autofocus.js',
    paths.src + 'javascripts/highlightTags.js',
    paths.src + 'javascripts/fileUpload.js',
    paths.src + 'javascripts/updateContent.js',
    paths.src + 'javascripts/expandCollapse.js',
    paths.src + 'javascripts/**/*.js',

  ])
  .pipe(plugins.babel({
    presets: ['es2015']
  }))
  .pipe(plugins.addSrc.prepend([
    paths.npm + 'jquery/dist/jquery.min.js',
    paths.npm + 'query-command-supported/dist/queryCommandSupported.min.js',
    paths.npm + 'diff-dom/diffDOM.js'
  ]))
  .pipe(plugins.concat('all.js'))
  .pipe(gulp.dest(paths.dist + 'javascripts/'))
);

gulp.task('sass', () => gulp
  .src(paths.src + 'stylesheets/main*.scss')
  .pipe(plugins.sass({
    outputStyle: 'compressed',
    includePaths: [
      paths.npm + 'govuk-elements-sass/public/sass/',
      paths.toolkit + 'stylesheets/'
    ]
  }))
  .pipe(plugins.base64({baseDir: 'apps'}))
  .pipe(gulp.dest(paths.dist + 'stylesheets/'))
);

// Copy images

gulp.task('images', () => gulp
  .src([
    paths.src + 'images/**/*',
    paths.toolkit + 'images/**/*',
    paths.template + 'assets/images/**/*'
  ])
  .pipe(gulp.dest(paths.dist + 'images/'))
);


// Watch for changes and re-run tasks
gulp.task('watchForChanges', function() {
  gulp.watch(paths.src + 'javascripts/**/*', ['javascripts']);
  gulp.watch(paths.src + 'stylesheets/**/*.scss', ['sass']);
  gulp.watch(paths.src + 'images/**/*', ['images']);
  gulp.watch('gulpfile.babel.js', ['default']);
});

gulp.task('lint:sass', () => gulp
  .src([
    paths.src + 'stylesheets/*.scss',
    paths.src + 'stylesheets/components/*.scss',
    paths.src + 'stylesheets/views/*.scss',
  ])
    .pipe(plugins.sassLint())
    .pipe(plugins.sassLint.format(stylish))
    .pipe(plugins.sassLint.failOnError())
);

gulp.task('lint:js', () => gulp
  .src(paths.src + 'javascripts/**/*.js')
    .pipe(plugins.jshint({'esversion': 6, 'esnext': false}))
    .pipe(plugins.jshint.reporter(stylish))
    .pipe(plugins.jshint.reporter('fail'))
);

gulp.task('lint',
  ['lint:sass', 'lint:js']
);

gulp.task('js:tests', () => {
    karma.server.start({
        configFile: __dirname + '/karma.conf.js',
    })
});

// Default: compile everything
gulp.task('default',
  [
    // 'copy:govuk_template:template',
    'copy:govuk_template:images',
    'copy:govuk_template:css',
    'copy:govuk_template:js',
    'javascripts',
    'sass',
    'images'
  ]
);

gulp.task('debug',
  [
    // 'copy:govuk_template:template',
    'copy:govuk_template:images',
    'copy:govuk_template:css',
    'copy:govuk_template:js',
    'debugjs',
    'sass',
    'images'
  ]
);


// Optional: recompile on changes
gulp.task('watch',
    ['default', 'watchForChanges']
);
