const fs = require("fs")

;(() => {
  const cwd = __dirname;
  const fileName = __filename;

  fs.readdir(cwd, (err, files) => {
    if (err) {
      console.log(err);
    }

    console.log(files);
  });
})();
