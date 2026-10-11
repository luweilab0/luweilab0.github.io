# Converts _data/publications.yml to _bibliography/papers.bib (jekyll-scholar).
# Author marks: "*" (corresponding) and "†" (co-first) are moved onto the BibTeX
# last name, matching the zhiwen10.github.io convention; bib_author.liquid
# renders them as superscripts.
require "yaml"

ABBR = {
  "Science" => "Science",
  "Cell" => "Cell",
  "Neuron" => "Neuron",
  "Nature" => "Nature",
  "Nature Neuroscience" => "Nat. Neurosci.",
  "Nature Aging" => "Nat. Aging",
  "Nature Communications" => "Nat. Commun.",
  "Journal of Neuroscience" => "J. Neurosci.",
  "Cell Reports" => "Cell Rep.",
  "Proceedings of the National Academy of Sciences USA" => "PNAS",
  "PLOS Biology" => "PLOS Biol.",
  "Trends in Neurosciences" => "Trends Neurosci.",
  "EMBO Reports" => "EMBO Rep.",
  "Neuropsychopharmacology" => "Neuropsychopharmacol.",
  "Molecular Psychiatry" => "Mol. Psychiatry",
  "Immunity" => "Immunity",
  "Journal of Clinical Investigation" => "JCI",
}.freeze

def bibtex_name(token)
  token = token.strip
  marks = ""
  while token =~ /[*†]\z/
    marks = token[-1] + marks
    token = token[0..-2].strip
  end
  return "others" if token.casecmp("et al.").zero?

  if token =~ /\ABadger JD 2nd\z/
    return "Badger, 2nd, JD"
  end
  parts = token.split(/\s+/)
  first = parts.pop # initials
  last = parts.join(" ") + marks
  "#{last}, #{first}"
end

def cite_key(first_author, year, title)
  last = first_author.split(",").first.gsub(/[^A-Za-z]/, "").downcase
  word = title.gsub(/[^A-Za-z0-9\s]/, "").split.first.to_s.downcase
  "#{last}#{year}#{word}"
end

pubs = YAML.load_file("_data/publications.yml")
out = +""
pubs.each do |p|
  authors = p["authors"].split(/,\s*/).map { |a| bibtex_name(a) }.join(" and ")
  title = p["title"].sub(/\.\z/, "")
  detail = p["detail"].to_s.strip
  volume = number = pages = note = nil
  case detail
  when /\A\((.+)\)\z/
    note = Regexp.last_match(1)
  when /\A(\d+)\(([^)]+)\),\s*(.+)\z/
    volume, number, pages = Regexp.last_match(1), Regexp.last_match(2), Regexp.last_match(3)
  when /\A(\d+)\(([^)]+)\)\z/
    volume, number = Regexp.last_match(1), Regexp.last_match(2)
  when /\A(\d+),\s*(.+)\z/
    volume, pages = Regexp.last_match(1), Regexp.last_match(2)
  else
    note = detail
  end
  key = cite_key(authors.split(" and ").first, p["year"], title)
  out << "@article{#{key},\n"
  out << "  abbr={#{ABBR[p['journal']]}},\n" if ABBR[p["journal"]]
  out << "  title={#{title}},\n"
  out << "  author={#{authors}},\n"
  out << "  journal={#{p['journal']}},\n"
  out << "  volume={#{volume}},\n" if volume
  out << "  number={#{number}},\n" if number
  out << "  pages={#{pages.gsub('-', '--')}},\n" if pages
  out << "  year={#{p['year']}},\n"
  out << "  note={#{note}},\n" if note
  out << "}\n\n"
end
File.write("_bibliography/papers.bib", out)
puts "wrote #{pubs.size} entries"
