// Client-side checks that mirror the Flask validation, so mistakes show
// before a round trip. The server still validates everything.
(function () {
  const form = document.querySelector("[data-contact-form]");
  if (!form) return;

  const rules = {
    name: (v) => (v ? "" : "Enter your name."),
    email: (v) => (/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(v) ? "" : "Enter an email address like name@example.com."),
    message: (v) => (v.length >= 10 ? "" : "Write at least 10 characters so I know how to help."),
  };

  function check(input) {
    const msg = rules[input.name](input.value.trim());
    const field = input.closest(".field");
    const out = field.querySelector(".field-error");
    out.textContent = msg;
    field.classList.toggle("has-error", Boolean(msg));
    if (msg) {
      input.setAttribute("aria-invalid", "true");
      input.setAttribute("aria-describedby", out.id);
    } else {
      input.removeAttribute("aria-invalid");
    }
    return !msg;
  }

  Object.keys(rules).forEach((name) => {
    const input = form.elements[name];
    input.addEventListener("blur", () => check(input));
    input.addEventListener("input", () => {
      if (input.closest(".field").classList.contains("has-error")) check(input);
    });
  });

  form.addEventListener("submit", (e) => {
    const results = Object.keys(rules).map((n) => check(form.elements[n]));
    if (results.includes(false)) {
      e.preventDefault();
      form.querySelector("[aria-invalid='true']").focus();
    } else {
      form.querySelector("button[type=submit]").textContent = "Sending…";
    }
  });
})();
